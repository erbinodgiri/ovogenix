FROM python:3.9-slim

WORKDIR /app

# Create a non-root user
RUN useradd -m -u 1000 appuser && chown appuser:appuser /app

# Install dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Switch to non-root user
USER appuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]