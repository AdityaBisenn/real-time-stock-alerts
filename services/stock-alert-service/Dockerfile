# Use Python 3.10 as base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 8002 for service communication
EXPOSE 8001

# Start API Gateway using Uvicorn with proper settings
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
