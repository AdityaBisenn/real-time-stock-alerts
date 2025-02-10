from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class StockAlert(Base):
    """Stock alert model"""
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    stock_symbol = Column(String, index=True)
    target_price = Column(Float, nullable=False)
    condition = Column(String, nullable=False)  # 'above' or 'below'
    is_active = Column(Boolean, default=True)
