# Sprint_n — UI-тесты "Яндекс.Маршруты"
- POM: src/pages/*
- Данные: src/data/*
- Утилиты/ожидания: src/utils/*
- Тесты: tests/*
## Запуск
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
## Allure
pytest --alluredir=allure-results
allure serve allure-results
