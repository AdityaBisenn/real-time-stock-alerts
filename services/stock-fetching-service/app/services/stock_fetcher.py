import requests
import app.core.logger as logger
import os

ALPHA_VANTAGE_API_KEY = "QBRC2CQELNH554P1"
API_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol: str):
    try:
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",
            "apikey": ALPHA_VANTAGE_API_KEY,
        }
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        time_series = data.get("Time Series (1min)")
        
        if not time_series:
            logger.logger.error(f"No data found for {symbol}. Response: {data}")
            return None

        latest_timestamp = sorted(time_series.keys())[-1]
        last_quote = float(time_series[latest_timestamp]["4. close"])
        
        return last_quote

    except Exception as e:
        logger.logger.error(f"Failed to fetch data for {symbol}: {e}")
        return None
