# 🧾 Scoring Service

**Warehouse Service** — сервис для чистого склада.

## 🚀 Возможности

- На складе есть товары, которые можно заказать за определенную цену. 
- Можно заказать сразу несколько товаров. 
- Заказы сохраняются в базе данных

## 📦 Установка

```bash
git clone https://github.com/NikitaKh/WarehouseService.git
cd WarehouseService
poetry install
```

## ⚙️ Пример запуска

```bash
poetry run python main.py
```

## 🧪 Тестирование

```bash
poetry run pytest
```

## 🔍 Проверки

```bash
poetry run pre-commit run --all-files
```

## 🛠️ CI

Проект включает GitHub Actions workflow (.github/workflows/main.yml), который запускает:

- black
- isort
- flake8
- pytest

при каждом пуше в main или pull request.
