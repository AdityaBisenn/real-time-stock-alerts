from fastapi import APIRouter, HTTPException
from app.core.logger import logger
from app.services.stock_fetcher import fetch_stock_data, get_stock_data
from app.services.kafka_producer import publish_stock_update

router = APIRouter()

@router.post("/api/fetch-stock-data")
async def fetch_data(stock_symbol: str):
    """Fetch stock data"""
    logger.info("Fetching stock data...")
    try:
        stock_price = await fetch_stock_data(stock_symbol)
        if stock_price is None:
            raise HTTPException(status_code=404, detail="Stock data not found")
        
        publish_stock_update(stock_symbol, stock_price)
        
        stock_data = {
            "symbol": stock_symbol,
            "price": stock_price
        }
        return stock_data
    except Exception as e:
        logger.error(f"Failed to fetch stock data: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch stock data")
    
@router.get("/api/get-stock-data")
async def get_stock_data_route(stock_symbol: str, interval: str = "1min"):
    """Get stock data"""
    logger.info("Getting stock data...")
    try:
        stock_data = await get_stock_data(stock_symbol, interval)
        if stock_data is None:
            raise HTTPException(status_code=404, detail="Stock data not found")
        return stock_data
    except Exception as e:
        logger.error(f"Failed to get stock data: {e}")
        raise HTTPException(status_code=500, detail="Failed to get stock data")
