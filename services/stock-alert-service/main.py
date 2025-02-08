from fastapi import FastAPI
from kafka import KafkaConsumer

app = FastAPI()

consumer = KafkaConsumer('stock_prices', bootstrap_servers='kafka:9092')

@app.get("/")
def home():
    return {"message": "Stock Alert Service Running"}

@app.get("/alerts")
def get_alerts():
    alerts = []
    for msg in consumer:
        alerts.append(msg.value.decode('utf-8'))
        if len(alerts) > 10:
            break
    return {"alerts": alerts}
