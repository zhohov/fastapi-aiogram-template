FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY pyproject.toml poetry.lock /backend/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /backend

EXPOSE 8000

CMD ["poetry", "run", "python", "src/main.py"]