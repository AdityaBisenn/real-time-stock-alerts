from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.core.db import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    alert_id = Column(Integer, ForeignKey("alerts.id"))
    stock_symbol = Column(String, nullable=False)
    message = Column(String, nullable=False)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
class StockAlert(Base):
    """Stock alert model"""
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    stock_symbol = Column(String, index=True)
    target_price = Column(Float, nullable=False)
    condition = Column(String, nullable=False)  # 'above' or 'below'
    is_active = Column(Boolean, default=True)
