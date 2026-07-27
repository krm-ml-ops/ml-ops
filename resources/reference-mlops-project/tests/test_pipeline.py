import json

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
