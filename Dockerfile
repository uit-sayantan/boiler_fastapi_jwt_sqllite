FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
COPY app/ app/
# Install system dependencies required for psycopg2-binary
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --proxy-headers

