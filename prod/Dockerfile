FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip "poetry==2.1.2"
RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY mysite .