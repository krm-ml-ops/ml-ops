# MLflow: лабораторный сценарий 05

MLflow является опциональным расширением эталонного проекта. Обычные тесты и `./scripts/verify.sh` не требуют его установки или запущенного сервера.

## Локальный tracking server

`uv` поставляется только root Nix development shell. Из корня репозитория выполните `nix develop`, затем в каталоге `resources/reference-mlops-project/` синхронизируйте дополнительную группу и запустите сервер с локальными хранилищами:

```bash
uv sync --extra mlflow
uv run mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlartifacts
```

В другом терминале укажите tracking URI, создайте данные и выполните обучение с логированием:

```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
uv run python -m reference_mlops.generate_data --output data/synthetic.csv --samples 500 --seed 42
uv run python -m reference_mlops.train --input data/synthetic.csv --model-output artifacts/model.pkl --metrics-output artifacts/metrics.json --mlflow
```

Откройте `http://127.0.0.1:5000`. Запуск `reference-mlops-training` содержит параметры имени и размера набора, `seed`, модель и долю тестовой выборки; метрики `accuracy` и `f1`; тэг `course_lab=lab-05`; и артефакты `model/model.pkl` и `metrics/metrics.json`.

## Доказательства и альтернатива

Для ЛР 05 студент сохраняет ссылку или экспорт списка минимум восьми сопоставимых запусков, параметры, метрики, выбранный run, артефакты и команду повторного запуска. Для восьми запусков изменяйте допустимые параметры варианта и присваивайте каждому содержательное имя через интерфейс MLflow или свой код варианта.

Локальный сервер с SQLite и файловым artifact store равнозначен удаленному сервису для целей работы: оба сохраняют runs, параметры, метрики и артефакты. При недоступности MLflow разрешается представить локальные JSON-метрики, модель, конфигурации и таблицу сравнения при тех же критериях рубрики. Удалите `mlflow.db`, `mlartifacts/`, `mlruns/`, `data/` и `artifacts/` после работы, если они больше не нужны.
