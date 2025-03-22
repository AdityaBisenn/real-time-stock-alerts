from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
# from app.db.database import SessionLocal
from app.db.database import get_notifications
from app.services.websocket import ws_manager
from app.core.db import get_db
from app.services.websocket import ws_manager

router = APIRouter()

@router.get("/notifications/{user_id}")
async def fetch_notifications(user_id: int, db: Session = Depends(get_db)):
    """Fetch past notifications for a user"""
    return get_notifications(user_id)

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    """WebSocket connection for real-time notifications"""
    await ws_manager.connect(websocket, user_id)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(user_id)

@router.post("/send-notification/{user_id}")
async def send_notification(user_id: int, message: str):
    """Send a real-time notification to a user"""
    return await ws_manager.send_notification_ws(user_id, message)
