from kafka import KafkaProducer
import json
from app.core.config import config
from app.core.logger import logger

producer = KafkaProducer(bootstrap_servers=config.KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def publish_notification_alert(notification_data):
    """Publish a notification alert to the Kafka topic"""
    try:
        producer.send("notification_alerts", value=notification_data)
        logger.info(f"Published notification alert to Kafka")
    except Exception as e:
        logger.error(f"Failed to publish notification alert to Kafka: {e}")