from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/stocks")
def fetch_stocks():
    response = requests.get("http://stock-fetching-service:8001")
    return response.json()
