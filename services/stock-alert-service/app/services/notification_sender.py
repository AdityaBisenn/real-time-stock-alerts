from app.core.logger import logger

def send_notification(user_id, symbol, price):
    """Send a notification to the user"""
    logger.info(f"Sending notification to user {user_id} for stock {symbol} at price {price}")
    # Send the notification to the user
    pass
    