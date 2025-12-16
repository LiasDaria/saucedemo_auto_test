# Saucedemo Login Tests

Автоматизированные UI-тесты авторизации для сайта https://www.saucedemo.com/

## Стек
- Python 3.10
- Playwright
- Pytest
- Allure
- Page Object Model
- Docker

# открываем терминал в PyCharm в контексте .venv
- pip install --upgrade pip
- pip install -r requirements.txt
- python -m playwright install
# проверяем установку
- python -m pytest --version
- python -m playwright --version
 # запуск тестов
 - python -m pytest tests/test_login.py --alluredir=allure-results

## Установка и запуск локально

```powershell
pip install -r requirements.txt
python -m playwright install
python -m pytest tests --alluredir=allure-results
