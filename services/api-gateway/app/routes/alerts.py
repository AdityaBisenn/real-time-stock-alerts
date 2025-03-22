from fastapi import APIRouter, HTTPException, Depends
from app.core.config import config
from app.core.security import get_current_user
from app.core.api_client import api_client  # Import the APIClient instance

router = APIRouter()

STOCK_SERVICE_URL = config.ALERT_SERVICE_URL  # Ensure correct service URL

@router.post("/create-alert")
async def create_alert(alert_data: dict, user: dict = Depends(get_current_user)):
    """Forward alert creation request to Stock Alert Service using APIClient"""
    alert_data['user_id'] = user['user_id']
    
    try:
        response = await api_client.post(f"{STOCK_SERVICE_URL}/api/create-alert", alert_data)
        return response
    except HTTPException as e:
        raise e  # Forward the HTTPException raised by APIClient
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create alert")
    
@router.get("/get-alerts")
async def get_alerts(user: dict = Depends(get_current_user)):
    """Forward get alert request to Stock Alert Service using APIClient"""
    try:
        user_id = user["user_id"]
        response = await api_client.get(f"{STOCK_SERVICE_URL}/api/get-alerts/{user_id}")
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to get alerts")
    
@router.get("/get-active-alerts")
async def get_active_alerts(user: dict = Depends(get_current_user)):
    """Forward get active alerts request to Stock Alert Service using APIClient"""
    try:
        user_id = user["user_id"]
        response = await api_client.get(f"{STOCK_SERVICE_URL}/api/get-active-alerts/{user_id}")
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to get active alerts")
