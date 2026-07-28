"""Evaluate a trained reference model against the prepared test split."""

import argparse
import json
import pickle
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from reference_mlops.generate_data import FEATURE_NAMES
from reference_mlops.prepare import load_dataset


def evaluate(
    input_path: Path,
    model_path: Path,
    metrics_output: Path,
    cv_input_path: Path | None = None,
    cv_folds: int = 5,
    seed: int = 42,
) -> dict[str, float]:
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
    if cv_input_path:
        cv_rows = load_dataset(cv_input_path)
        cv_features = [[float(row[name]) for name in FEATURE_NAMES] for row in cv_rows]
        cv_target = [int(row["target"]) for row in cv_rows]
        model = Pipeline(
            [("scale", StandardScaler()), ("classifier", LogisticRegression(random_state=seed, max_iter=200))]
        )
        scores = cross_validate(
            model,
            cv_features,
            cv_target,
            cv=StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=seed),
            scoring={"accuracy": "accuracy", "f1": "f1"},
        )
        metrics["cv_accuracy"] = round(float(scores["test_accuracy"].mean()), 6)
        metrics["cv_f1"] = round(float(scores["test_f1"].mean()), 6)
    metrics_output.parent.mkdir(parents=True, exist_ok=True)
    metrics_output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the reference model")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--metrics-output", type=Path, required=True)
    parser.add_argument("--cv-input", type=Path, help="prepared training data for cross-validation")
    parser.add_argument("--cv-folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    evaluate(args.input, args.model, args.metrics_output, args.cv_input, args.cv_folds, args.seed)


if __name__ == "__main__":
    main()
