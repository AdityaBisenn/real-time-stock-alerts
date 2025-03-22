from celery.schedules import crontab
from app.core.celery import celery
from app.core.logger import logger
from app.tasks.stock_tasks import fetch_stock_data_task
from app.db.database import get_target_list
import requests

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    """Fetch stock symbols dynamically and schedule periodic tasks every 5 minutes."""
    try:
        sender.add_periodic_task(
            crontab(minute="*/59"),  # Runs every 5 minutes
            fetch_all_stocks_task.s(),
            name="Fetch stock symbols & schedule tasks"
        )
    except Exception as e:
        logger.error(f"Error setting up periodic tasks: {e}")

@celery.task(queue='celery')
def fetch_all_stocks_task():
    """Fetch updated stock symbols and schedule fetch tasks."""
    try:
        # make api request to get stock symbols
        stock_symbols = requests.get("http://stock-alert-service:8001/api/get-target-list").json()
        if not stock_symbols:
            logger.warning("No stock symbols retrieved from get_target_list.")
            return

        logger.info(f"Fetched stock symbols: {stock_symbols}")

        for symbol in stock_symbols:
            fetch_stock_data_task.delay(symbol)  # Schedule data fetch
    except Exception as e:
        logger.error(f"Error fetching stock symbols: {e}")
