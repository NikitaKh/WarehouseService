.PHONY: run test lint format check-all coverage

# Запуск приложения
run:
	poetry run python main.py

# Запуск тестов
test:
	poetry run pytest

# Запуск тестов с покрытием
coverage:
	poetry run pytest --cov=infrastructure --cov-report=term

# Проверки: mypy + flake8
lint:
	poetry run flake8 infrastructure/ domain/ tests/

# Форматирование: black + isort
format:
	poetry run black .
	poetry run isort .

# Проверка форматирования и линтеров
check-all:
	poetry run black . --check
	poetry run isort . --check-only
	poetry run flake8 infrastructure/ domain/ tests/

# Синхронизация poetry
sync:
	poetry lock && poetry install
