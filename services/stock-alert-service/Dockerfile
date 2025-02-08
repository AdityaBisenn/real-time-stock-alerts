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
EXPOSE 8002

# Run the Kafka consumer service
CMD ["python", "kafka_consumer.py"]
