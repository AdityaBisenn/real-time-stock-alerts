from fastapi import FastAPI
from routes import stocks, notifications, alerts, auth
from core.logger import logger

app = FastAPI(title="Stock Market API Gateway", version="1.0")

# Register routes
app.include_router(stocks.router)
app.include_router(notifications.router)
app.include_router(alerts.router)
app.include_router(auth.router)

logger.info("API Gateway is running...")
