# Fundamentals of MLOps: Cleaned Course Program

## 1. General Course Information

| Field | Value |
|---|---|
| Course title | Fundamentals of MLOps |
| Institution | Moscow Technical University of Communications and Informatics (MTUCI) |
| Degree program | 09.03.01 Informatics and Computer Engineering |
| Program profile | TOP-AI: Engineering of Artificial Intelligence Systems |
| Qualification | Bachelor |
| Delivery mode | Full-time |
| Semester | 5 |
| Workload | 3 ECTS / 108 academic hours |
| Final assessment | Zachet |

## 2. Goal and Tasks

The course forms practical and system-level understanding of MLOps approaches for the full lifecycle of machine learning systems: data preparation, model training, versioning, testing, containerization, CI/CD, deployment, monitoring, and production support.

Key learning tasks:

1. Understand MLOps as a combination of DevOps, Data Engineering, and ML Engineering practices.
2. Build reproducible environments and containerized ML applications.
3. Design CI/CD workflows for ML projects.
4. Manage versions of data, models, experiments, and artifacts.
5. Deploy and monitor ML services with attention to reliability, security, and documentation.

## 3. Place in the Curriculum

The discipline belongs to the variable part of the degree program block and is delivered as `B1.V.06`. It supports later study in courses related to natural language processing, multi-agent systems, and final qualification work.

Students are expected to enter the course with basic Python programming skills, understanding of machine learning workflows, and familiarity with Git and command-line work in Linux or WSL.

## 4. Planned Learning Outcomes and Competencies

| Competency / indicator | Course focus |
|---|---|
| BD-5.1 | selecting infrastructure and toolchain components for ML work |
| BD-5.3 | testing, evaluating, and monitoring AI solutions |
| ML-2.2 | data preparation and feature processing in ML pipelines |
| DL-3.2 | building training and deployment pipelines for model-based services |
| PL-1.3 | implementing maintainable Python services and processing workflows |
| LC-3.1 | designing AI system architecture across lifecycle stages |
| LC-5.1 | choosing and applying engineering practices for ML deployment and support |

Expected outcomes after course completion:

1. Select and justify a practical MLOps stack for an ML project.
2. Implement reproducible training and delivery workflows.
3. Track experiments, datasets, models, and artifacts.
4. Deploy a model as an API service with validation and tests.
5. Monitor operational and model-related signals in production-like conditions.

## 5. Workload and Semester Structure

| Type of work | Hours |
|---|---:|
| Lectures | 18 |
| Laboratory works | 32 |
| Other contact work | 1 |
| Independent study | 53 |
| Total | 108 |

The course is delivered in semester 5. The final form of intermediate assessment is a zachet.

## 6. Thematic Plan

| Module | Topics | Lectures | Labs | Independent study | Total |
|---|---|---:|---:|---:|---:|
| Module 1. CI/CD and DevOps for ML | DevOps principles, CI/CD, Docker, infrastructure basics | 6 | 12 | 16 | 34 |
| Module 2. ML Lifecycle Management | ML pipelines, experiment tracking, data and model versioning | 6 | 12 | 16 | 34 |
| Module 3. Deployment, Monitoring, and Model Support | FastAPI deployment, monitoring, drift, support, documentation | 6 | 8 | 26 | 40 |
| Total |  | 18 | 32 | 58 | 108 |

## 7. Lecture and Lab Breakdown

### Module 1. CI/CD and DevOps for ML

- Lecture 1: Introduction to DevOps and CI/CD
- Lecture 2: Infrastructure as code, Docker, and virtualization
- Lecture 3: GitHub Actions and Jenkins for ML delivery
- Lab 01: Docker and reproducible environment setup
- Lab 02: Building Docker images and working with containers
- Lab 03: Creating a CI/CD pipeline for an ML project

### Module 2. ML Lifecycle Management

- Lecture 4: ML pipelines from data to model
- Lecture 5: Experiment tracking with MLflow
- Lecture 6: Data and model versioning with DVC
- Lab 04: Simple ML pipeline implementation
- Lab 05: Experiment tracking with MLflow
- Lab 06: Tracking data and model changes with DVC

### Module 3. Deployment, Monitoring, and Model Support

- Lecture 7: Deploying models as API services with FastAPI and Docker
- Lecture 8: Monitoring, logging, and A/B testing
- Lecture 9: Documentation, ethics, and service stability
- Lab 07: FastAPI service for a model
- Lab 08: Model monitoring with Prometheus and Grafana

## 8. Independent Study Guidance

Independent study includes:

- reviewing lecture notes and core literature;
- preparing for laboratory implementation and defense;
- studying official documentation for Docker, FastAPI, MLflow, DVC, Prometheus, and Grafana;
- completing missed tasks and refining reports;
- preparing for the final zachet.

Suggested self-study questions are derived from the official source materials and cover reproducibility, CI/CD, versioning, deployment, monitoring, drift, and lifecycle governance.

## 9. Assessment Materials Summary

The assessment model combines current and final control:

- current assessment through 8 labs and their defense;
- final zachet after all labs are completed;
- zachet components: theoretical questions, competence-oriented tests, and practical tasks where needed.

Detailed materials are published in [Exam/README.md](../Exam/README.md) and the module folders.

## 10. Learning and Information Resources

Core and recommended resources include:

- DevOps textbook by Kirillova and Mishina;
- Docker textbook by Elton Mouat;
- Yandex Machine Learning Handbook sections on MLOps;
- Full Stack Deep Learning course materials.

The repository version of these resources is curated in [resources/README.md](../resources/README.md).

## 11. Software and Infrastructure Requirements

Recommended student stack:

- Python 3.10+
- Git
- Docker Engine or Docker Desktop
- Linux or Windows with WSL2
- FastAPI
- MLflow
- DVC
- Prometheus and Grafana for monitoring labs

Students should be able to run projects from documented commands on a clean machine and must not commit secrets, tokens, or private data into the repository.

## 12. Accessibility and Inclusive Learning Guidance

The course may be adapted for students with disabilities and special educational needs. Delivery should support flexible formats, individual pacing where needed, and alternative presentation or submission formats without changing the academic goals of the discipline.

## 13. Student Methodological Recommendations

Students should maintain all source code, configuration, and run instructions in version control, document setup and launch steps clearly, and treat reproducibility as a graded quality attribute of every practical task.
