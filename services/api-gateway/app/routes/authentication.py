from fastapi import APIRouter, HTTPException, Depends
import requests
from app.core.config import config
from app.core.logger import logger
from app.core.security import get_current_user


router = APIRouter()

AUTH_SERVICE_URL = config.AUTH_SERVICE_URL

@router.post("/signup")
async def signup(user_data: dict):
    """Forward user signup request to Authentication Service"""
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/api/auth/signup/", json=user_data)
        data = response.json()
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Signup request failed: {e}")
        raise HTTPException(status_code=response.status_code, detail=data)

@router.post("/login")
async def login(credentials: dict):
    """Forward user login request and issue JWT"""
    logger.info(f"Forwarding login request to {AUTH_SERVICE_URL}")
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/api/auth/login/", json=credentials)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Login request failed: {e}")
        raise HTTPException(status_code=response.status_code, detail=response.json())

@router.post("/logout")
async def logout(token: str):
    """Blacklist JWT to prevent further use"""
    return {"message": "Logged out successfully"}


@router.get("/user/me")
async def get_user_info(user: dict = Depends(get_current_user)):
    return {"user": user}

@router.get("/profile")
async def get_profile(user: dict = Depends(get_current_user)):
    """Get user profile information"""
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/api/auth/profile/", headers={"Authorization": f"Bearer {user['access_token']}"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Profile request failed: {e}")
        raise HTTPException(status_code=response.status_code, detail=response.json())
