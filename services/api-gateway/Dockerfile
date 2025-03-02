# Use official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies file (e.g., requirements.txt or poetry.lock)
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN pip install --upgrade pip && pip install poetry && poetry install --no-root --no-dev

# Copy application code
COPY . .

# Expose API Gateway port
EXPOSE 8080

# Start API Gateway using Uvicorn with proper settings
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
