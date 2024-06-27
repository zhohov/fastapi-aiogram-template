FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /bot

COPY pyproject.toml poetry.lock /bot/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /bot

EXPOSE 8443

CMD ["poetry", "run", "python", "src/main.py"]