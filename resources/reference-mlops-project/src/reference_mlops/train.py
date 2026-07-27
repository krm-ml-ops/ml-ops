"""Train and serialize the reference classification model."""

import argparse
import csv
import json
import pickle
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from reference_mlops import __version__
from reference_mlops.generate_data import FEATURE_NAMES


def load_dataset(input_path: Path) -> tuple[list[list[float]], list[int]]:
    with input_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != [*FEATURE_NAMES, "target"]:
            raise ValueError("CSV must contain feature_0..feature_3 and target columns")
        rows = list(reader)
    if len(rows) < 10:
        raise ValueError("dataset must contain at least 10 rows")
    return (
        [[float(row[name]) for name in FEATURE_NAMES] for row in rows],
        [int(row["target"]) for row in rows],
    )


def train(input_path: Path, model_output: Path, metrics_output: Path, seed: int = 42) -> dict[str, float]:
    features, target = load_dataset(input_path)
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=seed, stratify=target
    )
    model = Pipeline([("scale", StandardScaler()), ("classifier", LogisticRegression(random_state=seed))])
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    metrics = {
        "accuracy": round(float(accuracy_score(y_test, predictions)), 6),
        "f1": round(float(f1_score(y_test, predictions)), 6),
    }
    bundle = {"model": model, "features": FEATURE_NAMES, "version": __version__, "metrics": metrics}
    model_output.parent.mkdir(parents=True, exist_ok=True)
    metrics_output.parent.mkdir(parents=True, exist_ok=True)
    with model_output.open("wb") as file:
        pickle.dump(bundle, file)
    metrics_output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Train the reference model")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--model-output", type=Path, required=True)
    parser.add_argument("--metrics-output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    train(args.input, args.model_output, args.metrics_output, args.seed)


if __name__ == "__main__":
    main()
