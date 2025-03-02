from app.core.logger import logger
from app.core.config import config
from app.services.kafka_producer import publish_notification_alert

def send_notification(user_id, symbol, price, alert_id):
    """Send a notification to the user"""
    try:
        notification_data = {
            "user_id": user_id,
            "symbol": symbol,
            "price": price,
            "alert_id": alert_id
        }
        publish_notification_alert(notification_data)
        logger.info(f"Sent notification to user {user_id} for symbol {symbol} at price {price}")
    except Exception as e:
        logger.error(f"Failed to send notification to user {user_id} for symbol {symbol} at price {price}: {e}")