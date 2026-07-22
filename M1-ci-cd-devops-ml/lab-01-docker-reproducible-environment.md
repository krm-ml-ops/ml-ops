# Lab 01. Docker and Reproducible Environment Setup

## Objective

Build a reproducible ML project environment and validate that the same workflow runs consistently on the host machine and inside a container.

## Tasks

1. Install and verify Docker and the local Python toolchain.
2. Create a minimal ML project structure with `src/`, `data/`, `tests/`, `requirements.txt`, `Dockerfile`, and `README.md`.
3. Pin project dependencies and document how the environment is recreated.
4. Build a Docker image and run a validation script inside the container.
5. Compare host and container execution results.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- Docker Engine or Docker Desktop
- Code editor or IDE

## Theory Summary

Reproducibility in MLOps depends on controlled versions of the interpreter, dependencies, and runtime environment. Docker images provide an immutable build artifact, while containers provide isolated runtime instances. For ML workflows, this reduces environment drift between development, CI, and deployment.

## Assignment

- Create `src/check_environment.py` to print Python and library versions, load a small dataset, and perform one preprocessing step.
- Prepare a `Dockerfile` based on the base image required by the assigned variant.
- Build the image with tag `mlops-lab1:<variant>`.
- Run the container with the `data/` directory mounted read-only.
- Record the differences, if any, between host and container execution.

## Individual Variants

Use one of the ten variants defined in `materials/md/лабораторные.md`, including the assigned dataset, base image, and mandatory dependencies.

## Report Requirements

- Goal and assigned variant
- Repository structure and key configuration files
- Build and run commands
- Evidence of successful execution on host and in container
- Problems encountered and how they were resolved
- Final conclusions on reproducibility

## Control Questions

1. What makes an ML environment reproducible?
2. How does a Docker image differ from a container?
3. Why should dependency versions be pinned?
4. What is the difference between `COPY` and a bind mount?
5. Why should secrets never be committed to the repository?

## Related Competencies and Indicators

- LC-5.1
- BD-5.1
