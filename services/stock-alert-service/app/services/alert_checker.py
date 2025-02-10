from app.db.database import get_active_alerts
from app.core.logger import logger
from app.services.notification_sender import send_notification

def check_alerts(stock_data):
    """Check the stock alerts"""
    try:
        symbol = stock_data["symbol"]
        price = stock_data["price"]

        alerts = get_active_alerts()

        for alert in alerts:
            if alert.stock_symbol == symbol:
                if alert.condition == "above" and price > alert.target_price:
                    send_notification(alert.user_id, symbol, price)
                elif alert.condition == "below" and price < alert.target_price:
                    send_notification(alert.user_id, symbol, price)
                else:
                    logger.info(f"Price for stock {symbol} did not meet the alert conditions")
            else:
                logger.info(f"Stock symbol {symbol} does not match any active alerts")
    except Exception as e:
        logger.error(f"Failed to check alerts: {e}")
    