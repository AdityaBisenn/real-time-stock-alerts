from fastapi import APIRouter, HTTPException
import os
from app.db import database
from app.core.logger import logger
from pydantic import BaseModel
from app.services.stock_fetcher import fetch_stock_data
from app.services.kafka_producer import publish_stock_update

router = APIRouter()

@router.post("/api/fetch-stock-data")
async def fetch_data(stock_symbol: str):
    """Fetch stock data"""
    logger.info("Fetching stock data...")
    try:
        stock_price = fetch_stock_data(stock_symbol)
        publish_stock_update(stock_symbol, stock_price)
        stock_data = {
            "symbol": stock_symbol,
            "price": stock_price
        }
        return stock_data
    except Exception as e:
        logger.error(f"Failed to fetch stock data: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch stock data")
        
