from fastapi import APIRouter, HTTPException
from services.http_client import fetch_data
import os


router = APIRouter()
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://stock-fetching-service:8001")

@router.post("/auth/login")
async def login(request):
    """Login to the application"""
    username = request.form.get("username")