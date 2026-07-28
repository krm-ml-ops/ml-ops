# Паспорт: Reference MLOps Synthetic Dataset

## Назначение и происхождение

Это синтетический набор бинарной классификации для эталонного проекта и ЛР 01, 04, 06-08; в ЛР 05 он может быть входом для сравнения экспериментов. Источник генератора - [`sklearn.datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html) из `scikit-learn==1.6.0`, закрепленного в [pyproject.toml](../reference-mlops-project/pyproject.toml). Документация scikit-learn опубликована под BSD 3-Clause; сгенерированный CSV является фактическим результатом алгоритма, а не копией внешнего набора. Перед повторным распространением производного набора следует сохранить это уведомление и условия используемых пакетов.

Набор не содержит персональных данных. Он не представляет предметную область, не отражает реальное распределение и не пригоден для принятия решений о людях, организациях или процессах. Синтетическая генерация может скрывать смещения, пропуски, drift и эксплуатационные ограничения реальных данных.

## Каноническая конфигурация

| Поле | Значение |
| --- | --- |
| Команда | `python -m reference_mlops.generate_data --output data/synthetic.csv --samples 500 --seed 42` |
| Генератор | [исходный код](../reference-mlops-project/src/reference_mlops/generate_data.py), `make_classification` |
| Версия и доступ | `scikit-learn==1.6.0`; пакет устанавливается через PyPI, доступ проверен 2026-07-27 |
| Число записей | 500 |
| Признаки | `feature_0` ... `feature_3`, четыре числа с плавающей точкой |
| Цель | `target`, целые классы `0` и `1` |
| Параметры генерации | `n_features=4`, `n_informative=2`, `n_redundant=0`, `n_classes=2`, `random_state=42` |
| Обучение baseline | стратифицированное разбиение 80/20, `random_state=42`, `LogisticRegression` |

Команда записывает CSV с заголовком и 500 строками; классы генерируются двумя классами `0`/`1`. Для получения воспроизводимой сводки выполните после генерации:

```bash
python -c "import csv; from collections import Counter; rows=list(csv.DictReader(open('data/synthetic.csv', newline=''))); columns=rows[0].keys(); print('rows:', len(rows)); [print(f'{name}: min={min(float(row[name]) for row in rows):.6f}, max={max(float(row[name]) for row in rows):.6f}') for name in columns if name != 'target']; print('target:', dict(sorted(Counter(row['target'] for row in rows).items())))"
```

## Целостность и хранение

CSV намеренно не коммитится: канонический результат полностью задают закрепленная версия пакета, исходный генератор, параметры и seed. Поэтому статический SHA-256 не публикуется: он стал бы недействительным при сознательном обновлении генератора или зависимости. Для конкретной сдачи студент фиксирует команду, версию `scikit-learn` и при необходимости вычисляет `sha256sum data/synthetic.csv` в отчете. Изменение любого из этих элементов означает новую ревизию набора и должно быть зафиксировано через DVC или эквивалентный журнал.
