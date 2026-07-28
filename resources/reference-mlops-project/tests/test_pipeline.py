import json

import pytest

from reference_mlops.generate_data import generate_dataset
from reference_mlops.evaluate import evaluate
from reference_mlops.prepare import prepare
from reference_mlops.train import train


def test_pipeline_stages_are_deterministic_and_write_outputs(tmp_path):
    first = tmp_path / "first.csv"
    second = tmp_path / "second.csv"
    generate_dataset(first, samples=100, seed=7)
    generate_dataset(second, samples=100, seed=7)
    assert first.read_bytes() == second.read_bytes()

    prepare(first, tmp_path / "train.csv", tmp_path / "test.csv", test_size=0.2, seed=42)
    model = tmp_path / "model.pkl"
    metrics_file = tmp_path / "metrics.json"
    train(tmp_path / "train.csv", model)
    metrics = evaluate(tmp_path / "test.csv", model, metrics_file)
    assert set(metrics) == {"accuracy", "f1"}
    assert model.is_file()
    assert json.loads(metrics_file.read_text()) == metrics


def test_evaluation_writes_cross_validation_metrics(tmp_path):
    dataset = tmp_path / "data.csv"
    generate_dataset(dataset, samples=100, seed=7)
    train_data = tmp_path / "train.csv"
    test_data = tmp_path / "test.csv"
    prepare(dataset, train_data, test_data, test_size=0.2, seed=42)
    model = tmp_path / "model.pkl"
    train(train_data, model)

    metrics = evaluate(test_data, model, tmp_path / "metrics.json", cv_input_path=train_data)

    assert set(metrics) == {"accuracy", "f1", "cv_accuracy", "cv_f1"}
    assert all(0 <= value <= 1 for value in metrics.values())


def test_training_logs_optional_mlflow_run(tmp_path, monkeypatch):
    mlflow = pytest.importorskip("mlflow")
    if not hasattr(mlflow, "start_run"):
        pytest.skip("MLflow optional dependency is not installed")
    tracking_uri = (tmp_path / "mlruns").as_uri()
    monkeypatch.setenv("MLFLOW_TRACKING_URI", tracking_uri)
    dataset = tmp_path / "data.csv"
    generate_dataset(dataset, samples=100, seed=7)

    model = tmp_path / "model.pkl"
    train(dataset, model)

    runs = mlflow.search_runs(output_format="list")
    assert len(runs) == 1
    assert runs[0].data.params["seed"] == "42"
    assert {artifact.path for artifact in mlflow.MlflowClient().list_artifacts(runs[0].info.run_id)} == {"model"}
