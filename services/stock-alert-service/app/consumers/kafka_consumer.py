from kafka import KafkaConsumer
import json
from app.services.alert_checker import check_alerts
from app.core.logger import logger
import threading
from app.core.config import config

KAFKA_BROKER_URL = config.KAFKA_BROKER
KAFKA_TOPIC = "stock_prices"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

def consume_stock_updates():
    """Listen for stock price updates and process alerts"""
    try:
        logger.info("Listening for stock price updates...")
        for message in consumer:
            stock_data = message.value
            logger.info(f"Received stock update: {stock_data}")
            check_alerts(stock_data)  # Check if alerts are triggered
    except Exception as e:
        logger.error(f"Error consuming stock updates: {e}")

def start_kafka_consumer():
    """Start the Kafka consumer"""
    consumer_thread = threading.Thread(target=consume_stock_updates, daemon=True)
    consumer_thread.start()
    logger.info("Kafka consumer started")
