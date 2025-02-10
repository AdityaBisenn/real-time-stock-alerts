import yfinance as yf
import app.core.logger as logger

def fetch_stock_data(symbol: str):
    try:
        ticker_yahoo = yf.Ticker(symbol)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        return last_quote
    except Exception as e:
        logger.logger.error(f"Failed to fetch data for {symbol}: {e}")
        return None