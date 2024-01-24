FROM python:3.12-alpine3.17

ENV POETRY_VERSION=1.4.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY . .
RUN poetry config virtualenvs.create false \
    && poetry add uvicorn[standard] \
    && poetry install --no-interaction --no-ansi

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "gunicorn", "-w", "4", "wsgi:app", "-b", "0.0.0.0:8000" ]
