# Эталонный минимальный MLOps-проект

Проект показывает полный, но компактный контур для курса: воспроизводимые данные, обучение, HTTP-инференс, метрики, контейнеризация, CI и декларации DVC/MLflow. Задача модели учебная: бинарно классифицировать синтетические наблюдения по четырём числовым признакам. Артефакты данных и модели не коммитятся.

## Быстрый старт

`uv` предоставляется только root Nix development shell. Из корня репозитория выполните `nix develop`, перейдите в этот каталог и синхронизируйте прикладные и тестовые зависимости из зафиксированного `uv.lock`:

```bash
uv sync --extra dev
uv run ./scripts/verify.sh
```

`verify.sh` запускает pytest через `uv`, генерирует данные, обучает модель и проверяет JSON-метрики во временном каталоге. Он не вызывает DVC или MLflow и удаляет все созданные файлы после завершения.

Shell поддерживается на Linux, macOS на Apple Silicon и WSL 2; Intel macOS не поддерживается, так как используемый nixpkgs прекращает эту платформу. На WSL 2 Nix и команды `uv` выполняются внутри Linux-дистрибутива. Shell не дает доступа к Docker daemon и не устанавливает monitoring services: на macOS используйте запущенный Docker Desktop, а в WSL 2 включите Docker Desktop WSL integration или настройте Linux Docker daemon.

## Локальный жизненный цикл

```bash
uv run python -m reference_mlops.generate_data --output data/synthetic.csv --samples 500 --seed 42
uv run python -m reference_mlops.train --input data/synthetic.csv --model-output artifacts/model.pkl --metrics-output artifacts/metrics.json
MODEL_PATH=artifacts/model.pkl uvicorn reference_mlops.api:app --reload
```

После запуска API доступны `GET /health`, `GET /model-info`, `POST /predict`, `POST /predict-batch` и `GET /metrics`.

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/predict -H 'content-type: application/json' -d '{"features":[0.1,-0.2,0.3,0.4]}'
```

`/health` всегда сообщает доступность процесса и отдельно состояние модели. Инференс и сведения о модели вернут `503`, пока файла модели нет. В `model.pkl` сериализованы sklearn `Pipeline`, порядок признаков, версия пакета и метрики `accuracy`/`f1`. Загружайте pickle только из доверенного источника.

## Воспроизводимость и тесты

Генератор использует `make_classification` с фиксированным seed, а обучение использует фиксированное стратифицированное разбиение и `LogisticRegression`. Тесты проверяют побайтовую детерминированность CSV, наличие модели и метрик, а также контракт API. Запуск: `uv run pytest`.

Версии зависимостей закреплены в `pyproject.toml` и `uv.lock`. Данные, модели, MLflow runs и локальные кэши исключены в `.gitignore`.

## Docker и наблюдаемость

```bash
docker compose up --build
```

Compose создаёт данные и модель только внутри контейнера API, затем поднимает API (`http://localhost:8000`), Prometheus (`http://localhost:9090`) и Grafana (`http://localhost:3000`, начальные учётные данные Grafana: `admin`/`admin`). Prometheus собирает `/metrics`; правило предупреждает о недоступности API более минуты и о 5xx выше 5% в течение пяти минут. В Grafana автоматически загружается дашборд с RPS, частотой предсказаний и p95 latency.

## DVC и MLflow (опционально)

`dvc.yaml` описывает стадии `generate` и `train`; он является декларацией и не участвует в стандартной проверке. В Nix shell DVC можно запустить без постоянной установки:

```bash
uvx --from dvc dvc init
uvx --from dvc dvc repro
```

Для ЛР 05 используйте [рабочий сценарий MLflow](mlflow/README.md). Он запускает tracking server и сохраняет реальные параметры, метрики и артефакты. MLflow импортируется только по `--mlflow` или при заданном `MLFLOW_TRACKING_URI`, поэтому базовый контур остается запускаемым без него.

## Структура

```text
src/reference_mlops/  генерация, обучение и FastAPI
tests/                модульные и API-тесты
scripts/verify.sh     проверка без DVC и MLflow
monitoring/           Prometheus alerts и Grafana provisioning/dashboard
.github/workflows/    CI, расположенный внутри эталонного проекта
```

Для реального проекта замените генератор проверяемым источником данных, добавьте валидацию схемы и дрейфа, безопасное хранилище моделей, аутентификацию API, централизованные логи и маршрутизацию оповещений.
