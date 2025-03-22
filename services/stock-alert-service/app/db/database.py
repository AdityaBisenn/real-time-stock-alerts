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

async def get_alerts(user_id):
    """"Get Alerts by user id"""
    db = next(get_db())
    alerts = db.query(StockAlert).filter(StockAlert.user_id == user_id).all()
    db.close()
    return alerts

async def delete_alert(alert_id):
    """"Delete alert by alert id"""
    db = next(get_db())
    alerts = db.query(StockAlert).filter(StockAlert.id == alert_id).all()
    db.close()
    return alerts

def get_active_alerts(symbol):
    """Fetch all active alerts"""
    db = next(get_db())
    data = db.query(StockAlert).filter(StockAlert.stock_symbol == symbol, StockAlert.is_active == True).all()
    db.close()
    return data

async def get_active_alert_by_user(user_id):
    """Fetch active alerts by user"""
    db = next(get_db())
    data = db.query(StockAlert).filter(StockAlert.user_id == user_id, StockAlert.is_active==True).all()
    db.close()
    return data

async def get_target_list():
    db = next(get_db())
    data = db.query(StockAlert.stock_symbol).filter(StockAlert.is_active == True).distinct().all()
    db.close()
    return [stock[0] for stock in data][1:]
