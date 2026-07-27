#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
WORKDIR=$(mktemp -d)
trap 'rm -rf "$WORKDIR"' EXIT

PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" uv run --project "$ROOT" python -m pytest "$ROOT/tests"
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" uv run --project "$ROOT" python -m reference_mlops.generate_data --output "$WORKDIR/raw.csv" --samples 100 --seed 42
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" uv run --project "$ROOT" python -m reference_mlops.prepare --input "$WORKDIR/raw.csv" --train-output "$WORKDIR/train.csv" --test-output "$WORKDIR/test.csv" --test-size 0.2 --seed 42
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" uv run --project "$ROOT" python -m reference_mlops.train --input "$WORKDIR/train.csv" --model-output "$WORKDIR/model.pkl" --seed 42 --max-iter 200
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" uv run --project "$ROOT" python -m reference_mlops.evaluate --input "$WORKDIR/test.csv" --model "$WORKDIR/model.pkl" --metrics-output "$WORKDIR/metrics.json"
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" uv run --project "$ROOT" python -c 'import json, sys; print(json.load(open(sys.argv[1])))' "$WORKDIR/metrics.json"
