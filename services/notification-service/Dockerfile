# Use Python 3.10 as base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 8003 for WebSocket connections
EXPOSE 8003

# Run the WebSocket service
CMD ["python", "websocket_server.py"]
