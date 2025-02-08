from celery import Celery

app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@app.task
def fetch_stock_price(symbol):
    # Simulate fetching stock data
    return f"Stock price for {symbol} is 100"


from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_stock_price(symbol):
    # Simulate fetching stock data
    stock_price = {"symbol": symbol, "price": 100}
    producer.send("stock_prices", stock_price)
    return stock_price
