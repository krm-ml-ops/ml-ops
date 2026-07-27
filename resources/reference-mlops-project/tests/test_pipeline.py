import json

import pytest

from reference_mlops.generate_data import generate_dataset
from reference_mlops.train import train


def test_generation_is_deterministic_and_training_writes_outputs(tmp_path):
    first = tmp_path / "first.csv"
    second = tmp_path / "second.csv"
    generate_dataset(first, samples=100, seed=7)
    generate_dataset(second, samples=100, seed=7)
    assert first.read_bytes() == second.read_bytes()

    metrics = train(first, tmp_path / "model.pkl", tmp_path / "metrics.json")
    assert set(metrics) == {"accuracy", "f1"}
    assert (tmp_path / "model.pkl").is_file()
    assert json.loads((tmp_path / "metrics.json").read_text()) == metrics


def test_training_logs_optional_mlflow_run(tmp_path, monkeypatch):
    mlflow = pytest.importorskip("mlflow")
    tracking_uri = (tmp_path / "mlruns").as_uri()
    monkeypatch.setenv("MLFLOW_TRACKING_URI", tracking_uri)
    dataset = tmp_path / "data.csv"
    generate_dataset(dataset, samples=100, seed=7)

    metrics = train(dataset, tmp_path / "model.pkl", tmp_path / "metrics.json")

    runs = mlflow.search_runs(output_format="list")
    assert len(runs) == 1
    assert runs[0].data.params["seed"] == "42"
    assert runs[0].data.metrics == metrics
    assert {artifact.path for artifact in mlflow.MlflowClient().list_artifacts(runs[0].info.run_id)} == {
        "metrics",
        "model",
    }
