import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    STOCK_API_URL = os.getenv("STOCK_API_URL", "https://api.example.com/stocks")
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    CELERY_BROKER = os.getenv("CELERY_BROKER", "redis://redis:6379/0")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

config = Config()