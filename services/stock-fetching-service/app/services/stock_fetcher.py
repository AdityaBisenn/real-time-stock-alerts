import httpx
from app.core.logger import logger

TWELVEDATA_API_KEY = "9764e76f6ee24424931944be50a35339"
API_URL = "https://api.twelvedata.com/time_series"

async def fetch_stock_data(symbol: str):
    """Fetch the latest stock price."""
    try:
        params = {
            "symbol": symbol,
            "interval": "1min",
            "apikey": TWELVEDATA_API_KEY,
            "outputsize": 1,
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL, params=params)
            response.raise_for_status()
        
        data = response.json()
        values = data.get("values")
        
        if not values:
            logger.error(f"No data found for {symbol}. Response: {data}")
            return None
        
        latest_quote = float(values[0]["close"])
        return latest_quote
    
    except Exception as e:
        logger.error(f"Failed to fetch data for {symbol}: {e}")
        return None


async def get_stock_data(symbol: str, interval: str = "1min"):
    """Get historical stock data and parse it into a structured format."""
    try:
        params = {
            "symbol": symbol,
            "interval": interval,
            "apikey": TWELVEDATA_API_KEY,
            "outputsize": 80,
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL, params=params)
            response.raise_for_status()
        
        data = response.json()
        values = data.get("values")
        
        if not values:
            logger.error(f"No data found for {symbol}. Response: {data}")
            return None

        # Convert the raw API response into a list of formatted dictionaries
        formatted_data = [
            {
                "date": item["datetime"],
                "open": float(item["open"]),
                "high": float(item["high"]),
                "low": float(item["low"]),
                "close": float(item["close"]),
                "volume": int(item["volume"]),
            }
            for item in values
        ]

        return formatted_data

    except Exception as e:
        logger.error(f"Failed to get data for {symbol}: {e}")
        return None
