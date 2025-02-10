from app.services.redis_client import RedisClient

redis_client = RedisClient()

def get_stock_price(stock_symbol : str):
    """Receive a stock symbol and return the stock price from the cache if it exists, otherwise fetch it from the API and store it in the"""
    cached_price = redis_client.get(f'stock:{stock_symbol}')
    if cached_price:
        return cached_price
    price = fetch_stock_data(stock_symbol)
    if price:
        redis_client.set(stock_symbol, price)
    return price

def fetch_stock_data(symbol):
    # This function is already defined in services/stock-fetching-service/app/services/stock_fetcher.py
    pass