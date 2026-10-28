FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && python -m pip install --no-cache-dir --upgrade pip \
    && useradd --create-home --shell /usr/sbin/nologin appuser \
    && rm -rf /var/lib/apt/lists/*

COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]