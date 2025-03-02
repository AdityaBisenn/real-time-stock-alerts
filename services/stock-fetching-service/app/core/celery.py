from celery import Celery
from app.core.config import config

REDIS_BROKER_URL = config.CELERY_BROKER

celery = Celery(
    "stock_fetcher",
    broker=REDIS_BROKER_URL,
    backend=REDIS_BROKER_URL
)

celery.conf.update(
    task_routes={
        "app.tasks.stock_tasks.fetch_stock_data_task": {"queue": "stock_queue"},
    },
    timezone="UTC",
)

celery.autodiscover_tasks(['app.tasks.stock_tasks'])

# Import tasks to ensure they are registered
import app.tasks.stock_tasks 
import app.core.celery_tasks