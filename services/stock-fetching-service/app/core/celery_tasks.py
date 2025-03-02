from celery.schedules import crontab
from app.core.celery import celery
from datetime import datetime, timedelta
from app.core.logger import logger
import requests
from app.tasks.stock_tasks import fetch_stock_data_task

STOCK_SYMBOLS = ["AAPL", "TSLA", "AMZN"]
# API_URL = "http://localhost:8002/api/fetch-stock-data"

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    """Schedule stock fetching tasks periodically via API."""
    try:
        # Get current time and calculate 3 minutes from now
        # start_time = datetime.utcnow() + timedelta(minutes=2)

        for symbol in STOCK_SYMBOLS:
            try:
                # Run task **every 1 minute** after the first execution
                sender.add_periodic_task(
                    crontab(minute="*/10"),  # Every t minute
                    fetch_stock_data_task.s(symbol),  # Correct task signature
                    name=f"Fetch {symbol} stock data every 1 min",
                )
            except Exception as e:
                logger.error(f"Error scheduling task for {symbol}: {e}")
    except Exception as e:
        logger.error(f"Error setting up periodic tasks: {e}")
