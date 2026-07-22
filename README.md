# Fundamentals of MLOps

This repository publishes the course structure, assessment materials, and methodological support for the discipline `Fundamentals of MLOps`.

## Course Overview

- Institution: Moscow Technical University of Communications and Informatics (MTUCI)
- Degree program: `09.03.01 Informatics and Computer Engineering`
- Profile: `TOP-AI: Engineering of Artificial Intelligence Systems`
- Qualification: Bachelor
- Delivery mode: full-time
- Semester: 5
- Workload: `3 ECTS / 108 academic hours`
- Final assessment: `zachet`

## Goal

The course develops practical MLOps skills for the full lifecycle of machine learning systems: reproducible environments, containerization, CI/CD, experiment tracking, data and model versioning, deployment, monitoring, and production support.

## Key Learning Tasks

1. Understand MLOps as a combination of DevOps, Data Engineering, and ML Engineering practices.
2. Build reproducible ML environments and containerized services.
3. Automate quality checks, testing, and delivery with CI/CD.
4. Manage experiments, datasets, models, and artifacts across the ML lifecycle.
5. Deploy models as API services and monitor them in operation.

## Course Structure

### Module 1. CI/CD and DevOps for ML

- [Module overview](M1-ci-cd-devops-ml/README.md)
- Lab 01: [Docker and reproducible environment setup](M1-ci-cd-devops-ml/lab-01-docker-reproducible-environment.md)
- Lab 02: [Building Docker images and working with containers](M1-ci-cd-devops-ml/lab-02-docker-images-and-containers.md)
- Lab 03: [Creating a CI/CD pipeline for an ML project](M1-ci-cd-devops-ml/lab-03-ci-cd-pipeline.md)

### Module 2. ML Lifecycle Management

- [Module overview](M2-ml-lifecycle/README.md)
- Lab 04: [Simple ML pipeline implementation](M2-ml-lifecycle/lab-04-ml-pipeline.md)
- Lab 05: [Experiment tracking with MLflow](M2-ml-lifecycle/lab-05-mlflow-experiment-tracking.md)
- Lab 06: [Tracking data and model changes with DVC](M2-ml-lifecycle/lab-06-dvc-data-model-versioning.md)

### Module 3. Deployment, Monitoring, and Model Support

- [Module overview](M3-deployment-monitoring/README.md)
- Lab 07: [FastAPI service for a model](M3-deployment-monitoring/lab-07-fastapi-model-service.md)
- Lab 08: [Model monitoring with Prometheus and Grafana](M3-deployment-monitoring/lab-08-monitoring-prometheus-grafana.md)

## Planned Learning Outcomes

By the end of the course, students should be able to:

1. Choose an appropriate MLOps toolchain for a training and serving workflow.
2. Build reproducible ML pipelines and track experiments and artifacts.
3. Version datasets, models, and pipeline stages in a controlled way.
4. Deploy models as maintainable API services.
5. Monitor service health and early signs of model degradation.

## Assessment Summary

- Ongoing assessment: 8 laboratory works with implementation and defense
- Admission to final assessment: all labs completed and defended
- Final assessment: [zachet materials](Exam/README.md)
- Total score: 100 points
- Pass threshold: 60 points

## Main Repository Sections

- [Cleaned course program](docs/rpd.md)
- [Methodical guidelines](methodical-guidelines/README.md)
- [Curated resources](resources/README.md)
- [Project folder status](Project/README.md)
- [Quality checklist](docs/quality-checklist.md)
- [Team metadata](team/README.md) - TODO placeholders remain where source data is not available

## Notes

- `materials/` remains the source archive used to build this published structure.
- `Project/` is preserved in the repository but is not used as a separate assessment element for this discipline.
