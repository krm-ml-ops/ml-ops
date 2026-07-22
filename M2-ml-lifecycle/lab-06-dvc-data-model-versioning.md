# Lab 06. Tracking Data and Model Changes with DVC

## Objective

Version datasets, models, and pipeline stages with DVC and reproduce past ML states together with Git revisions.

## Tasks

1. Initialize DVC in a Git-based ML project.
2. Configure a remote storage location outside the repository.
3. Track datasets and model outputs with DVC.
4. Describe the workflow in `dvc.yaml`.
5. Compare metrics across revisions and restore a previous state.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- DVC
- Code editor or IDE

## Theory Summary

Git is effective for source code and lightweight metadata, while DVC extends version control to large datasets, trained models, and reproducible pipelines. Together, Git tags and DVC metadata make it possible to recover both code and data state for a given experiment.

## Assignment

- Initialize Git and DVC.
- Configure a local remote directory outside the repository.
- Add source data under DVC control and push it to the remote.
- Define at least `prepare`, `train`, and `evaluate` stages in `dvc.yaml`.
- Commit metadata files for one baseline version, modify the data according to the assigned variant, and compare metrics across versions.
- Restore a previous tagged revision with `dvc pull` and verify reproducibility.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned data change scenario, evaluation metric, and analysis goal.

## Report Requirements

- DVC setup and remote configuration
- Pipeline graph and tracked artifacts
- Comparison of at least two revisions
- Evidence of restoring a prior version
- Conclusions on data and model traceability

## Control Questions

1. Why should large datasets not be stored directly in Git?
2. What is stored in a `.dvc` file?
3. How does `dvc.yaml` differ from `dvc.lock`?
4. What do `deps` and `outs` represent?
5. How do Git revisions and DVC versions work together?

## Related Competencies and Indicators

- BD-5.3
- ML-2.2
- PL-1.3
