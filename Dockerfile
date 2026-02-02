FROM python:3.12-slim

WORKDIR /app

COPY . .

ARG IMAGE_TAG=latest
ENV IMAGE_TAG=${IMAGE_TAG}

ENV TELEGRAM_TOKEN=""
ENV TELEGRAM_CHAT_ID=""

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry install --no-interaction --no-root \
    && poetry run python -m playwright install --with-deps

ENTRYPOINT ["poetry", "run", "python"]
CMD ["run.py"]