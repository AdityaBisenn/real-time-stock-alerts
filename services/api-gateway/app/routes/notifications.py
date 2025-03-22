from fastapi import WebSocket, WebSocketDisconnect, HTTPException, status, APIRouter, Depends
import websockets
import asyncio
from app.core.security import verify_jwt, get_current_user
from app.core.logger import logger
from app.core.api_client import api_client

router = APIRouter()

NOTIFICATION_SERVICE_WS_URL = "ws://notification-service:8003/ws"
NOTIFICATION_SERVICE_URL = "http://notification-service:8003"

@router.websocket("/ws")
async def websocket_proxy(websocket: WebSocket):
    # Extract token from query parameters
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    
    # JWT Verification
    try:
        payload = verify_jwt(token)
        user_id = payload.get("user_id")
        if not user_id:
            logger.error("JWT token does not contain user_id")
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return
    except HTTPException as e:
        logger.error(f"JWT verification failed: {e.detail}")
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    # Accept WebSocket connection
    await websocket.accept()

    # Connect to the backend notification service
    try:
        async with websockets.connect(f"{NOTIFICATION_SERVICE_WS_URL}/{user_id}") as backend_ws:

            async def client_to_backend():
                try:
                    async for message in websocket.iter_text():
                        await backend_ws.send(message)
                except WebSocketDisconnect:
                    logger.info(f"Client WebSocket disconnected for user {user_id}")

            async def backend_to_client():
                try:
                    async for message in backend_ws:
                        await websocket.send_text(message)
                except Exception as e:
                    logger.error(f"Backend WebSocket error: {e}")

            # Run both tasks concurrently
            await asyncio.gather(client_to_backend(), backend_to_client())

    except Exception as e:
        logger.error(f"WebSocket proxy error for user {user_id}: {e}")
        await websocket.close(code=status.WS_1011_INTERNAL_ERROR)

@router.get("/")
async def getNotification(user = Depends(get_current_user)):
    user_id = user.get("user_id")
    url = f"{NOTIFICATION_SERVICE_URL}/notifications/{user_id}"
    response = await api_client.get(url)
    return response
