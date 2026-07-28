"""Evaluate a trained reference model against the prepared test split."""

import argparse
import json
import pickle
from pathlib import Path

from sklearn.metrics import accuracy_score, f1_score

from reference_mlops.generate_data import FEATURE_NAMES
from reference_mlops.prepare import load_dataset


def evaluate(input_path: Path, model_path: Path, metrics_output: Path) -> dict[str, float]:
    """Write deterministic classification metrics for the held-out data."""
    rows = load_dataset(input_path)
    features = [[float(row[name]) for name in FEATURE_NAMES] for row in rows]
    target = [int(row["target"]) for row in rows]
    with model_path.open("rb") as file:
        bundle = pickle.load(file)
    predictions = bundle["model"].predict(features)
    metrics = {
        "accuracy": round(float(accuracy_score(target, predictions)), 6),
        "f1": round(float(f1_score(target, predictions)), 6),
    }
    metrics_output.parent.mkdir(parents=True, exist_ok=True)
    metrics_output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the reference model")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--metrics-output", type=Path, required=True)
    args = parser.parse_args()
    evaluate(args.input, args.model, args.metrics_output)


if __name__ == "__main__":
    main()
