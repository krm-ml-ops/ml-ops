# Lab 03. Creating a CI/CD Pipeline for an ML Project

## Objective

Automate quality checks, testing, build, and delivery steps for an ML project using a reproducible CI/CD pipeline.

## Tasks

1. Add automated code and data quality checks.
2. Configure CI to run tests and verify a minimum model-quality threshold.
3. Build the Docker image only after validation succeeds.
4. Publish an artifact or simulate deployment under controlled conditions.
5. Demonstrate both successful and failing pipeline behavior.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- Docker Engine or Docker Desktop
- GitHub Actions or Jenkins
- Code editor or IDE

## Theory Summary

CI focuses on automated verification of every change, while CD prepares or performs delivery. In ML systems, pipelines should validate not only application code but also data assumptions, training reproducibility, and model-quality thresholds.

## Assignment

- Add at least two unit tests and one data-quality test.
- Add a linter, formatter check, or static analysis step.
- Implement a workflow or Jenkins pipeline according to the assigned variant.
- Cache Python dependencies.
- Train on a reduced dataset during CI and fail the pipeline if the required metric threshold is not met.
- Build the Docker image after successful checks.
- Archive test reports and metrics as CI artifacts.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned CI system, checks, metric threshold, and delivery rule.

## Report Requirements

- Pipeline stages and triggers
- Checks included and their rationale
- Artifact and metric retention
- Evidence of one successful and one failing run
- Conclusion on readiness for team development

## Control Questions

1. What triggers a CI pipeline?
2. How does CI differ from CD?
3. Which checks are especially important for ML projects?
4. Why should model-quality checks not replace unit tests?
5. How are registry credentials handled safely in CI/CD?

## Related Competencies and Indicators

- BD-5.3
- DL-3.2
- LC-5.1
