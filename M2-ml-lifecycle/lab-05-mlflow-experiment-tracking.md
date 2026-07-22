# Lab 05. Experiment Tracking with MLflow

## Objective

Use MLflow to track experiments, compare model runs, and register the best candidate for further lifecycle stages.

## Tasks

1. Deploy a local MLflow Tracking Server.
2. Run a parameterized experiment grid.
3. Log metrics, parameters, artifacts, and runtime context.
4. Compare runs and justify the best result.
5. Register the selected model and verify loading it back.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- MLflow
- Code editor or IDE

## Theory Summary

Experiment tracking is essential for comparing runs, understanding model behavior, and ensuring that training decisions are explainable and reproducible. MLflow connects parameters, metrics, artifacts, and registered models across the ML lifecycle.

## Assignment

- Launch MLflow with local backend and artifact stores.
- Create an experiment named using the group and variant convention.
- Execute at least eight runs over a parameter grid.
- Log train and test metrics, parameters, seed, artifacts, and training duration.
- Register the best model and assign alias `candidate`.
- Load the model from MLflow and perform a control inference.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned model family, search parameters, and primary selection metric.

## Report Requirements

- Tracking server configuration
- Run comparison table
- Best-model selection rationale
- Registered model evidence
- Notes on reproducibility of the chosen run

## Control Questions

1. What is an MLflow run?
2. How do parameters differ from metrics?
3. What belongs in artifact storage?
4. Why should seed and data split be logged?
5. Why is the best offline metric not always the best production model?

## Related Competencies and Indicators

- BD-5.3
- ML-2.2
- LC-5.1
