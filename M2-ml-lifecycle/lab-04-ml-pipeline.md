# Lab 04. Simple ML Pipeline Implementation

## Objective

Implement a reproducible ML pipeline from data loading to model persistence with explicit validation, configuration, and metrics.

## Tasks

1. Split the workflow into clear processing stages.
2. Separate configuration from code.
3. Validate input data before training.
4. Prevent data leakage in preprocessing.
5. Save the model, configuration, and evaluation metrics.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- scikit-learn
- pandas
- PyYAML or JSON-based configuration tooling

## Theory Summary

An ML pipeline formalizes the sequence from raw data to evaluated model artifacts. Clear stage boundaries improve debugging, repeatability, and future automation. Configuration-driven execution is a prerequisite for reliable experiment management and lifecycle control.

## Assignment

- Implement `load`, `validate`, `split`, `preprocess`, `train`, `evaluate`, and `save` stages.
- Store parameters in YAML or JSON.
- Validate schema, missing values, and ranges.
- Use `sklearn.pipeline.Pipeline` or an equivalent functional design.
- Save the trained model, metrics, configuration, and data-version information.
- Add at least two automated tests.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned dataset, pipeline design, and target metrics.

## Report Requirements

- Pipeline architecture and configuration design
- Validation strategy
- Saved artifacts and reproducibility notes
- Test evidence and measured metrics
- Lessons learned about pipeline modularity

## Control Questions

1. Which stages typically belong to an ML pipeline?
2. What is data leakage?
3. Why should preprocessing be fit only on training data?
4. Why keep configuration outside the source code?
5. Which pipeline stages benefit most from automated tests?

## Related Competencies and Indicators

- ML-2.2
- PL-1.3
- LC-3.1
