# Saucedemo Login Tests

Автоматизированные UI-тесты авторизации для сайта https://www.saucedemo.com/

## Стек
- Python 3.10
- Playwright
- Pytest
- Allure
- Page Object Model
- Docker

## Установка и запуск локально

```powershell
pip install -r requirements.txt
python -m playwright install
python -m pytest tests --alluredir=allure-results