from fastapi import FastAPI
from app.core.db import engine, Base
from app.core.logger import logger
from app.db.database import create_tables
from app.routes import alerts
from app.consumers.kafka_consumer import start_kafka_consumer

# Initialize FastAPI application
app = FastAPI(
    title="Stock Alert Service",
    description="Microservice for managing stock alerts",
    version="1.0.0"
)

# Register API routes
app.include_router(alerts.router)

# Startup event for initializing the database
@app.on_event("startup")
def on_startup():
    create_tables()
    start_kafka_consumer()
    logger.info("Stock Alert Service is running...")

