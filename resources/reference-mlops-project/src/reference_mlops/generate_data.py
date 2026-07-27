"""Deterministic synthetic data generator."""

import argparse
import csv
from pathlib import Path

from sklearn.datasets import make_classification


FEATURE_NAMES = [f"feature_{index}" for index in range(4)]


def generate_dataset(output: Path, samples: int = 500, seed: int = 42) -> None:
    """Write a reproducible binary-classification CSV file."""
    if samples < 10:
        raise ValueError("samples must be at least 10")
    features, target = make_classification(
        n_samples=samples,
        n_features=len(FEATURE_NAMES),
        n_informative=2,
        n_redundant=0,
        n_classes=2,
        random_state=seed,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([*FEATURE_NAMES, "target"])
        writer.writerows([*row, int(label)] for row, label in zip(features, target))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic synthetic data")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    generate_dataset(args.output, args.samples, args.seed)


if __name__ == "__main__":
    main()
