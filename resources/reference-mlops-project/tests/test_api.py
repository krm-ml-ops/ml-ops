from fastapi.testclient import TestClient

from reference_mlops.api import create_app
from reference_mlops.generate_data import generate_dataset
from reference_mlops.train import train


def test_prediction_endpoints(tmp_path):
    data = tmp_path / "data.csv"
    model = tmp_path / "model.pkl"
    generate_dataset(data, samples=100)
    train(data, model)
    client = TestClient(create_app(model))

    assert client.get("/health").json()["model"] == "ready"
    assert client.get("/model-info").status_code == 200
    response = client.post("/predict", json={"features": [0.1, -0.2, 0.3, 0.4]})
    assert response.status_code == 200
    assert response.json()["prediction"] in (0, 1)
    batch = client.post(
        "/predict-batch",
        json={"items": [{"features": [0.1, -0.2, 0.3, 0.4]}, {"features": [0.2, 0.1, 0.0, -0.4]}]},
    )
    assert batch.status_code == 200
    assert len(batch.json()["predictions"]) == 2
    assert "model_predictions_total" in client.get("/metrics").text
