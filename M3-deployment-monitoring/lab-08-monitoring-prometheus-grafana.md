# Lab 08. Model Monitoring with Prometheus and Grafana

## Objective

Instrument an ML service, collect technical and model-related metrics, and analyze system behavior using Prometheus and Grafana.

## Tasks

1. Expose service metrics from the FastAPI application.
2. Deploy Prometheus and Grafana with Docker Compose.
3. Build a dashboard for service and model behavior.
4. Generate normal traffic, spikes, and invalid requests.
5. Configure and validate alerting rules.

## Required Software

- Linux or Windows 10/11 with WSL2
- Python 3.10+
- Git
- Docker Compose
- Prometheus
- Grafana
- `prometheus-client`

## Theory Summary

Monitoring in MLOps covers infrastructure, service behavior, and model behavior. Since true labels often arrive late, operational monitoring also relies on proxy indicators such as prediction distributions, input drift, latency, and error rates.

## Assignment

- Extend the Lab 07 service with a `/metrics` endpoint.
- Add request counters, latency histograms, active-request gauges, and error counters.
- Add at least two model-related metrics defined by the assigned variant.
- Configure Docker Compose for the service, Prometheus, and Grafana.
- Create a Grafana dashboard with at least six panels.
- Define one technical alert and one model alert, trigger both intentionally, and document the outcome.

## Individual Variants

Use the variant matrix from `materials/md/лабораторные.md`, including the assigned model metric and alert thresholds.

## Report Requirements

- Monitoring architecture and scrape configuration
- Dashboard overview
- Alert rules and proof of triggering
- Analysis of service health and possible model degradation
- Final recommendations

## Control Questions

1. Which metric groups matter in ML monitoring?
2. How does a `Counter` differ from a `Gauge`?
3. When is a `Histogram` preferable?
4. Why is label cardinality important?
5. Why is model monitoring harder when ground truth is delayed?

## Related Competencies and Indicators

- BD-5.1
- BD-5.3
- LC-5.1
