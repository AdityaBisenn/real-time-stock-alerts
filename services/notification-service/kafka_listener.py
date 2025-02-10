from kafka import KafkaConsumer
import json
from fastapi import WebSocket

consumer = KafkaConsumer(
    "alerts",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

clients = []  # Store connected WebSocket clients

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        for message in consumer:
            alert = message.value
            for client in clients:
                await client.send_json(alert)
    except Exception as e:
        clients.remove(websocket)
