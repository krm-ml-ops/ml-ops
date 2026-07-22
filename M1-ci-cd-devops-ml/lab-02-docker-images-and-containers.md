# Lab 02. Building Docker Images and Working with Containers

## Objective

Design a practical and maintainable Docker image for an ML application and manage container lifecycle operations.

## Tasks

1. Implement a small training or inference application.
2. Optimize the Docker build for caching, size, and repeatability.
3. Configure runtime parameters through environment variables.
4. Add a health check and persist artifacts outside the container.
5. Inspect and measure the resulting container behavior.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- Docker Engine or Docker Desktop
- Code editor or IDE

## Theory Summary

Container quality is measured not only by correctness, but also by rebuild speed, image size, security, and operational clarity. Proper Docker layering, `.dockerignore`, non-root execution, and explicit runtime configuration are core MLOps practices.

## Assignment

- Implement `train.py` or `predict.py` according to the assigned variant.
- Create `.dockerignore`.
- Build a Docker image with efficient layer reuse; use multi-stage build where the variant requires it.
- Expose configuration through environment variables and command-line arguments.
- Save generated artifacts into a mounted `/artifacts` directory.
- Demonstrate `docker inspect`, `docker logs`, `docker exec`, and `docker stats` during validation.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned application type, build mode, environment parameter, and output artifact.

## Report Requirements

- Build strategy and image structure
- Runtime configuration and artifact handling
- Image size and repeat build behavior
- Evidence of health check and container inspection
- Conclusions on security and maintainability

## Control Questions

1. Why does instruction order matter in a `Dockerfile`?
2. What is the purpose of `.dockerignore`?
3. When is a multi-stage build useful?
4. Why should artifacts usually live outside the container filesystem?
5. What reduces the attack surface of a containerized service?

## Related Competencies and Indicators

- LC-5.1
- BD-5.3
