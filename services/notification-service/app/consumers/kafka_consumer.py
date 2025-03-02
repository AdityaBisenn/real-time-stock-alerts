from kafka import KafkaConsumer
import json
import asyncio
import threading
from app.core.logger import logger
from app.core.config import config
from app.services.notification_sender import send_notification

KAFKA_BROKER_URL = config.KAFKA_BROKER
KAFKA_TOPIC = "notification_alerts"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

async def consume_notification_alerts():
    """Listen for notification alerts and process them"""
    try:
        logger.info("Listening for notification alerts...")
        for message in consumer:
            notification_data = message.value
            logger.info(f"Received notification alert: {notification_data}")
            await send_notification(notification_data)  # Send the notification to the user
    except Exception as e:
        logger.error(f"Error consuming notification alerts: {e}")

def start_kafka_consumer():
    """Start the Kafka consumer in a separate thread with an event loop"""
    def run():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(consume_notification_alerts())

    consumer_thread = threading.Thread(target=run, daemon=True)
    consumer_thread.start()
    logger.info("Kafka consumer started")
