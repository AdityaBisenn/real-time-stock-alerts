from sqlalchemy.orm import Session
from app.db.models import Notification, StockAlert
from app.schemas.notification import NotificationCreate
from app.core.logger import logger
from app.core.db import Base, engine
from app.core.db import get_db
from sqlalchemy import text

def create_tables():
    """Create database tables if they do not exist."""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")


async def create_notification(user_id: int, stock_symbol: str, message: str):
    try:
        db = next(get_db())
        notification = Notification(user_id=user_id, stock_symbol=stock_symbol, message=message)
        db.add(notification)
        db.commit()
        db.refresh(notification)
        db.close()
        return notification
    except Exception as e:
        db.rollback()
        raise e

def get_notifications(user_id: int):
    try:
        db = next(get_db())
        notifications = db.query(Notification).filter(Notification.user_id == user_id).all()
        db.close()
        return notifications
    except Exception as e:
        raise e
    
async def update_alert_status(alert_id: int):
    try:
        db = next(get_db())
        alert = db.query(StockAlert).filter(StockAlert.id == alert_id).first()
        alert.is_active = False
        db.commit()
        db.refresh(alert)
        return alert
    except Exception as e:
        db.rollback()
        raise e
    
async def get_user_details(user_id: int):
    try:
        db = next(get_db())
        query = text("SELECT * FROM users_customuser WHERE id = :user_id") 
        result = db.execute(query, {"user_id": user_id}).fetchone()
        db.close()
        return result
    except Exception as e:
        raise e
