FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m playwright install --with-deps

COPY . .

CMD ["python", "-m", "pytest", "tests", "--alluredir=allure-results"]