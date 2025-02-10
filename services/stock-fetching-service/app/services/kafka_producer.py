from kafka import KafkaProducer
import json
from app.core.config import config
from app.core.logger import logger

producer = KafkaProducer(bootstrap_servers=config.KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def publish_stock_update(stock_symbol, stock_price):
    """Publish a stock update to the Kafka topic"""
    try:
        message = {
            "symbol": stock_symbol,
            "price": stock_price
        }
        producer.send("stock_prices", value=message)
        logger.info(f"Published stock update for {stock_symbol} to Kafka")
    except Exception as e:
        logger.error(f"Failed to publish stock update to Kafka: {e}")