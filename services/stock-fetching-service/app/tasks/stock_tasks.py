from app.core.celery import celery
from app.core.logger import logger
import requests

STOCK_SYMBOLS = ["AAPL", "GOOGL", "TSLA", "AMZN"]
API_URL = "http://stock-fetching-service:8002/api/fetch-stock-data"

@celery.task(queue='celery')
def fetch_stock_data_task(stock_symbol: str):
    """Celery task to fetch stock data from FastAPI service via API request."""
    try:
        logger.info(f"Fetching stock data for {stock_symbol} via API...")
        response = requests.post(API_URL, params={"stock_symbol": stock_symbol})

        if response.status_code == 200:
            stock_data = response.json()
            logger.info(f"Fetched stock data: {stock_data}")
        else:
            logger.error(f"Failed to fetch stock data: {response.text}")
    except Exception as e:
        logger.error(f"Error fetching stock data: {e}") 