"""Validate and deterministically split the synthetic dataset."""

import argparse
import csv
from pathlib import Path

from sklearn.model_selection import train_test_split

from reference_mlops.generate_data import FEATURE_NAMES


def load_dataset(input_path: Path) -> list[dict[str, str]]:
    """Read a dataset with the schema used by the reference project."""
    with input_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != [*FEATURE_NAMES, "target"]:
            raise ValueError("CSV must contain feature_0..feature_3 and target columns")
        rows = list(reader)
    if len(rows) < 10:
        raise ValueError("dataset must contain at least 10 rows")
    try:
        for row in rows:
            [float(row[name]) for name in FEATURE_NAMES]
            if int(row["target"]) not in (0, 1):
                raise ValueError("target must be binary")
    except (TypeError, ValueError) as error:
        raise ValueError("dataset contains invalid feature or target values") from error
    return rows


def write_dataset(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[*FEATURE_NAMES, "target"])
        writer.writeheader()
        writer.writerows(rows)


def prepare(input_path: Path, train_output: Path, test_output: Path, test_size: float, seed: int) -> None:
    """Validate input and create a reproducible stratified train/test split."""
    rows = load_dataset(input_path)
    train_rows, test_rows = train_test_split(
        rows,
        test_size=test_size,
        random_state=seed,
        stratify=[row["target"] for row in rows],
    )
    write_dataset(train_rows, train_output)
    write_dataset(test_rows, test_output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and split a dataset")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--train-output", type=Path, required=True)
    parser.add_argument("--test-output", type=Path, required=True)
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    prepare(args.input, args.train_output, args.test_output, args.test_size, args.seed)


if __name__ == "__main__":
    main()
