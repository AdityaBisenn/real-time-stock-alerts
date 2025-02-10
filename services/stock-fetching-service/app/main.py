from fastapi import FastAPI
from app.core.logger import logger
from app.routes import fetch_data

# Initialize FastAPI application
app = FastAPI(
    title="Stock Fetching Service",
    description="Microservice for fetching stock data",
    version="1.0.0"
)

# Register API routes
app.include_router(fetch_data.router)

# Startup event for initializing the database
@app.on_event("startup")
def on_startup():
    logger.info("Stock Fetching Service is running...")

