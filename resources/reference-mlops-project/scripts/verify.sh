#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
WORKDIR=$(mktemp -d)
trap 'rm -rf "$WORKDIR"' EXIT

PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" python -m pytest "$ROOT/tests"
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" python -m reference_mlops.generate_data --output "$WORKDIR/data.csv" --samples 100 --seed 42
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" python -m reference_mlops.train --input "$WORKDIR/data.csv" --model-output "$WORKDIR/model.pkl" --metrics-output "$WORKDIR/metrics.json"
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" python -c 'import json, sys; print(json.load(open(sys.argv[1])))' "$WORKDIR/metrics.json"
