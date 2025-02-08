from fastapi import APIRouter, HTTPException
from services.http_client import fetch_data
import os

router = APIRouter()
STOCK_FETCH_SERVICE_URL = os.getenv("STOCK_FETCH_SERVICE_URL", "http://stock-fetching-service:8001")

@router.get("/auth/{symbol}")
async def get_stock_data(symbol: str):
    """Fetch stock price from Stock Fetching Service"""
    url = f"{STOCK_FETCH_SERVICE_URL}/stocks/{symbol}"
    return await fetch_data(url)
