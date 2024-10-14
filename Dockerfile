FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.4.20 /uv /bin/uv

ADD . /app

WORKDIR /app
RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "main.py"]
