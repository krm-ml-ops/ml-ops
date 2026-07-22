# Lab 07. FastAPI Service for a Model

## Objective

Deploy a trained ML model as a documented REST API with validation, testing, and containerized execution.

## Tasks

1. Design a stable API contract for inference.
2. Load the model at application startup.
3. Implement single and batch prediction endpoints.
4. Validate inputs and handle errors explicitly.
5. Test and containerize the service.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- FastAPI
- Uvicorn
- pytest
- httpx

## Theory Summary

Model serving separates inference from the training environment and exposes a stable contract to consumers. FastAPI is well suited for educational MLOps because it combines Pydantic-based validation, generated API documentation, and testable endpoint structure.

## Assignment

- Prepare a serialized model and input schema.
- Implement `GET /health` and `GET /model-info`.
- Implement `POST /predict` and `POST /predict-batch`.
- Add request and response schemas with validation ranges and examples.
- Load the model once at startup and avoid repeated initialization.
- Add at least six tests, including invalid-input cases.
- Build and run the containerized service and verify the OpenAPI UI.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned model type, request shape, and response format.

## Report Requirements

- API contract and schema design
- Error handling and logging strategy
- Test coverage summary
- Container run evidence and sample requests
- Performance notes from repeated requests

## Control Questions

1. Why is Pydantic useful in ML APIs?
2. Why should the model be loaded once at startup?
3. What is the difference between health and readiness checks?
4. Which HTTP status codes fit validation errors and internal failures?
5. Why should raw request data be logged carefully?

## Related Competencies and Indicators

- LC-5.1
- DL-3.2
- BD-5.3
