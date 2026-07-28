"""Train and serialize the reference classification model."""

import argparse
import os
import pickle
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from reference_mlops import __version__
from reference_mlops.generate_data import FEATURE_NAMES
from reference_mlops.prepare import load_dataset


def log_mlflow_run(input_path: Path, model_output: Path, seed: int) -> None:
    """Log an optional MLflow run without making MLflow a baseline dependency."""
    try:
        import mlflow
    except ImportError as error:
        raise RuntimeError("MLflow was requested; install it with pip install '.[mlflow]'.") from error

    try:
        with mlflow.start_run(run_name="reference-mlops-training"):
            mlflow.set_tag("course_lab", "lab-05")
            mlflow.log_params(
                {
                    "dataset": input_path.name,
                    "dataset_rows": len(load_dataset(input_path)),
                    "seed": seed,
                    "model": "LogisticRegression",
                }
            )
            mlflow.log_artifact(str(model_output), artifact_path="model")
    except Exception as error:
        raise RuntimeError("MLflow logging failed; verify MLFLOW_TRACKING_URI and server access.") from error


def train(
    input_path: Path,
    model_output: Path,
    seed: int = 42,
    max_iter: int = 200,
    mlflow_enabled: bool = False,
) -> None:
    """Fit a model using only the prepared training split."""
    rows = load_dataset(input_path)
    features = [[float(row[name]) for name in FEATURE_NAMES] for row in rows]
    target = [int(row["target"]) for row in rows]
    model = Pipeline(
        [("scale", StandardScaler()), ("classifier", LogisticRegression(random_state=seed, max_iter=max_iter))]
    )
    model.fit(features, target)
    bundle = {"model": model, "features": FEATURE_NAMES, "version": __version__, "metrics": {}}
    model_output.parent.mkdir(parents=True, exist_ok=True)
    with model_output.open("wb") as file:
        pickle.dump(bundle, file)
    if mlflow_enabled or os.environ.get("MLFLOW_TRACKING_URI"):
        log_mlflow_run(input_path, model_output, seed)


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the reference model")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--model-output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max-iter", type=int, default=200)
    parser.add_argument("--mlflow", action="store_true", help="log this run to MLflow")
    args = parser.parse_args()
    train(args.input, args.model_output, args.seed, args.max_iter, args.mlflow)


if __name__ == "__main__":
    main()
