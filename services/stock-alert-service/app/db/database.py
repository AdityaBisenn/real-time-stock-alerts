from app.core.db import get_db
from app.db.models import StockAlert
from app.core.db import Base, engine
from app.core.logger import logger

# Initialize the database tables
def create_tables():
    """Create database tables if they do not exist."""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")

async def create_alert(user_id, stock_symbol, target_price, condition):
    """Create a new stock alert"""
    db = next(get_db())
    alert = StockAlert(user_id=user_id, stock_symbol=stock_symbol, target_price=target_price, condition=condition)
    db.add(alert)
    db.commit()
    db.refresh(alert)
    db.close()
    return alert

def get_active_alerts():
    """Fetch all active alerts"""
    db = next(get_db())
    data = db.query(StockAlert).filter(StockAlert.is_active==True).all()
    db.close()
    return data
