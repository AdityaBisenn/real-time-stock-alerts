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
        
# route for get alerts by user_id
@router.get("/api/get-alerts/{user_id}")
async def get_alerts(user_id: int):
    """Get all alerts for a user"""
    logger.info("Getting alerts for user {user_id}")
    try:
        alerts = await database.get_alerts(user_id)
        return alerts
    except Exception as e:
        logger.error(f"Failed to get alerts: {e}")
        raise HTTPException(status_code=500, detail="Failed to get alerts")
    
#  route for delete alert
@router.delete("/api/delete-alert/{alert_id}")
async def delete_alert(user_id: int, alert_id: int):
    """"Delete Alert"""
    try:
        alerts = await database.get_alerts(user_id)
        return alerts
    except Exception as e:
        logger.error(f"Failed to get alerts: {e}")
        raise HTTPException(status_code=500, detail="Failed to get alerts")
    
@router.get("/api/get-active-alerts/{user_id}")
async def get_active_alerts(user_id: int):
    """Get all active alerts"""
    try:
        alerts = await database.get_active_alert_by_user(user_id)
        return alerts
    except Exception as e:
        logger.error(f"Failed to get active alerts: {e}")
        raise HTTPException(status_code=500, detail="Failed to get active alerts")
    
@router.get("/api/get-target-list")
async def get_target_list():
    """Get all active alerts"""
    try:
        alerts = await database.get_target_list()
        return alerts
    except Exception as e:
        logger.error(f"Failed to get target list: {e}")
        raise HTTPException(status_code=500, detail="Failed to get target list")