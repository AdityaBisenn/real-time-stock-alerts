from app.core.logger import logger
from app.services.websocket import ws_manager
from app.db.database import update_alert_status, create_notification
from app.services.mailer import send_email

async def send_notification(notification_data):
    """Send a notification to the user"""
    try:
        logger.info(f"Sending notification to user {notification_data['user_id']} for symbol {notification_data['symbol']}")
        await ws_manager.send_notification_ws(notification_data["user_id"], f"Stock {notification_data['symbol']} at price {notification_data['price']}")
        logger.info(f"Sending notification to user {notification_data['user_id']} for symbol {notification_data['symbol']} at price {notification_data['price']}")
        await send_email(notification_data["user_id"], notification_data["symbol"], notification_data["price"])
        logger.info(f"Email sent to user {notification_data['user_id']} for symbol {notification_data['symbol']} at price {notification_data['price']}")
        await create_notification(notification_data["user_id"], notification_data["symbol"], notification_data["price"])
        logger.info(f"Notification created for user {notification_data['user_id']} for symbol {notification_data['symbol']} at price {notification_data['price']}")
        await update_alert_status(notification_data["alert_id"])
        logger.info(f"Alert {notification_data['alert_id']} updated successfully")
    except Exception as e:
        logger.error(f"Failed to send notification to user {notification_data['user_id']} for symbol {notification_data['symbol']} at price {notification_data['price']}: {e}")
