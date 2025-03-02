from app.core.logger import logger
from app.services.websocket import ws_manager

async def send_notification(notification_data):
    """Send a notification to the user"""
    try:
        logger.info(f"Sending notification to user {notification_data['user_id']} for symbol {notification_data['symbol']}")
        await ws_manager.send_notification_ws(notification_data["user_id"], f"Stock {notification_data['symbol']} at price {notification_data['price']}")
        logger.info(f"Sending notification to user {notification_data['user_id']} for symbol {notification_data['symbol']} at price {notification_data['price']}")
    except Exception as e:
        logger.error(f"Failed to send notification to user {notification_data['user_id']} for symbol {notification_data['symbol']} at price {notification_data['price']}: {e}")
