# Teacher Guidelines for Resources

## Recommended Software Stack

- Python 3.10+
- Git
- Docker Engine or Docker Desktop
- Linux or Windows with WSL2
- FastAPI
- MLflow
- DVC
- Prometheus and Grafana

## Environment Setup Expectations

The teaching environment should support container builds, local API serving, basic CI workflows, and local or simulated monitoring. If cloud infrastructure is unavailable, all labs should still remain executable on a local workstation.

## Platform Notes

- Linux is the reference environment.
- Windows setups should use WSL2 where possible.
- Docker permissions and mounted-volume behavior should be explained before Lab 01.
- Local registry, MLflow, and DVC remotes may be simulated with local directories and containers.

## Topic-Aligned References

- Docker official documentation for Labs 01-02
- GitHub Actions or Jenkins documentation for Lab 03
- scikit-learn pipeline documentation for Lab 04
- MLflow documentation for Lab 05
- DVC documentation for Lab 06
- FastAPI documentation for Lab 07
- Prometheus and Grafana documentation for Lab 08

## Teaching Support Strategy

Use small public datasets and lightweight local infrastructure first. The course goal is to build disciplined engineering habits around ML systems rather than large-scale distributed training.
