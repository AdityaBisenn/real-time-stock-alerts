from sqlalchemy.orm import Session
from app.db.models import Notification
from app.schemas.notification import NotificationCreate
from app.core.logger import logger
from app.core.db import Base, engine

def create_tables():
    """Create database tables if they do not exist."""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")


def create_notification(db: Session, user_id: int, stock_symbol: str, message: str):
    try:
        notification = Notification(user_id=user_id, stock_symbol=stock_symbol, message=message)
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return notification
    except Exception as e:
        db.rollback()
        raise e

def get_notifications(db: Session, user_id: int):
    try:
        return db.query(Notification).filter(Notification.user_id == user_id).all()
    except Exception as e:
        raise e
