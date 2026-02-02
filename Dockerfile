FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry install --no-interaction --no-root \
    && poetry run python -m playwright install --with-deps

ENV TELEGRAM_TOKEN=""
ENV TELEGRAM_CHAT_ID=""

CMD ["poetry", "run", "python", "src/etl.py"]