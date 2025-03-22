import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    STOCK_API_URL = os.getenv("STOCK_API_URL", "https://api.example.com/stocks")
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    CELERY_BROKER = os.getenv("CELERY_BROKER", "redis://redis:6379/0")

    DB_NAME = "stock_alerts"
    DB_USER = "user"
    DB_PASSWORD = "password"
    DB_HOST = "postgres"
    DB_PORT = "5432"

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "mayankdowner@gmail.com")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "your-email-password")
    MAIL_FROM = os.getenv("MAIL_FROM", "mayankdowner@gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")

config = Config()
