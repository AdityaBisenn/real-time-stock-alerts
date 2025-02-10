from fastapi import APIRouter, HTTPException
import os
from app.db import database
from app.core.logger import logger
from pydantic import BaseModel
from app.schemas.alert import AlertCreate

router = APIRouter()

@router.post("/api/create-alert")
async def create_alert(alert_data: AlertCreate):
    """Create an alert for a stock"""
    logger.info("Creating alert...")
    try:
        user_id = alert_data.user_id
        stock_symbol = alert_data.stock_symbol
        target_price = alert_data.target_price
        condition = alert_data.condition
        alert = await database.create_alert(user_id, stock_symbol, target_price, condition)
        return alert
    except Exception as e:
        logger.error(f"Failed to create alert: {e}")
        raise HTTPException(status_code=500, detail="Failed to create alert")
        
