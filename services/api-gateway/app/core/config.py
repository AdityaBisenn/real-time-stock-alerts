import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_PREFIX = "/api"
    AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://authentication-service:8000")
    STOCK_SERVICE_URL = os.getenv("STOCK_SERVICE_URL", "http://stock-fetching-service:8002")
    ALERT_SERVICE_URL = os.getenv("ALERT_SERVICE_URL", "http://stock-alert-service:8001")
    NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8003")
    NOTIFICATION_SERVICE_WS_URL = os.getenv("NOTIFICATION_SERVICE_WS_URL", "ws://notification-service:8003")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecret")
    JWT_ALGORITHM = "HS256"

config = Config()
