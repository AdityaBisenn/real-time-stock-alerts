import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://authentication-service:8000")
    STOCK_FETCH_SERVICE_URL = os.getenv("STOCK_FETCH_SERVICE_URL", "http://stock-fetching-service:8001")
    ALERT_SERVICE_URL = os.getenv("ALERT_SERVICE_URL", "http://stock-alert-service:8002")
    NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8003")

config = Config()
