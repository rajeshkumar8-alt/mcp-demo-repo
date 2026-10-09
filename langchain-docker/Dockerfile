# Stage 1: Builder

FROM python:3.13-slim AS builder

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock  README.md ./

COPY src ./src

RUN uv sync --frozen --no-dev


# Stage 2: Runtime

FROM python:3.13-slim AS runtime

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

COPY src ./src

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "src.langchain_docker.app:app", "--host", "0.0.0.0", "--port", "8000"]