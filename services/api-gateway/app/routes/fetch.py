from fastapi import APIRouter, HTTPException, Depends
import requests
from app.core.config import config
from app.core.api_client import api_client
from app.core.logger import logger

router = APIRouter()

STOCK_SERVICE_URL = config.STOCK_SERVICE_URL

@router.get("/get-stock-data")
async def get_stock_data(stock_symbol: str, interval: str = "1min"):
    """Get stock data"""
    logger.info("Getting stock data...")
    try:
        response = await api_client.get(f"{STOCK_SERVICE_URL}/api/get-stock-data?stock_symbol={stock_symbol}&interval={interval}")
        return response
    except HTTPException as e:
        logger.error(f"Failed to get stock data: {e}")
        raise e
    except Exception as e:
        logger.error(f"Failed to get stock data: {e}")
        raise HTTPException(status_code=500, detail="Failed to get stock data")

