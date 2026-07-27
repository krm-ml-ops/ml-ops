"""FastAPI inference service with Prometheus instrumentation."""

import os
import pickle
import time
from functools import lru_cache
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from pydantic import BaseModel, Field
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest


REQUESTS = Counter("http_requests_total", "HTTP requests", ["method", "path", "status"])
LATENCY = Histogram("http_request_duration_seconds", "HTTP request latency", ["path"])
PREDICTIONS = Counter("model_predictions_total", "Predictions produced", ["class_label"])


class PredictRequest(BaseModel):
    features: list[float] = Field(..., description="Values in the model feature order")


class PredictBatchRequest(BaseModel):
    items: list[PredictRequest] = Field(..., min_length=1, max_length=100)


@lru_cache(maxsize=4)
def load_bundle(model_path: Path) -> dict[str, Any]:
    with model_path.open("rb") as file:
        return pickle.load(file)


def create_app(model_path: Path | None = None) -> FastAPI:
    path = model_path or Path(os.getenv("MODEL_PATH", "artifacts/model.pkl"))
    app = FastAPI(title="Reference MLOps API", version="0.1.0")

    @app.middleware("http")
    async def observe_requests(request: Request, call_next: Any) -> Response:
        started = time.perf_counter()
        response = await call_next(request)
        route = request.url.path
        REQUESTS.labels(request.method, route, response.status_code).inc()
        LATENCY.labels(route).observe(time.perf_counter() - started)
        return response

    def bundle_or_503() -> dict[str, Any]:
        if not path.is_file():
            raise HTTPException(status_code=503, detail="model is not available")
        return load_bundle(path)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "model": "ready" if path.is_file() else "unavailable"}

    @app.get("/model-info")
    def model_info() -> dict[str, Any]:
        bundle = bundle_or_503()
        return {"version": bundle["version"], "features": bundle["features"], "metrics": bundle["metrics"]}

    @app.post("/predict")
    def predict(request: PredictRequest) -> dict[str, int]:
        bundle = bundle_or_503()
        if len(request.features) != len(bundle["features"]):
            raise HTTPException(status_code=422, detail=f"expected {len(bundle['features'])} feature values")
        prediction = int(bundle["model"].predict([request.features])[0])
        PREDICTIONS.labels(str(prediction)).inc()
        return {"prediction": prediction}

    @app.post("/predict-batch")
    def predict_batch(request: PredictBatchRequest) -> dict[str, list[int]]:
        bundle = bundle_or_503()
        expected_count = len(bundle["features"])
        if any(len(item.features) != expected_count for item in request.items):
            raise HTTPException(status_code=422, detail=f"expected {expected_count} feature values per item")
        predictions = [int(value) for value in bundle["model"].predict([item.features for item in request.items])]
        for prediction in predictions:
            PREDICTIONS.labels(str(prediction)).inc()
        return {"predictions": predictions}

    @app.get("/metrics", include_in_schema=False)
    def metrics() -> Response:
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

    return app


app = create_app()
