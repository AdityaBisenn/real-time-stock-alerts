from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "stock_prices",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

for message in consumer:
    stock = message.value
    print(f"Received stock update: {stock}")
    # Add logic to check if alert conditions are met
