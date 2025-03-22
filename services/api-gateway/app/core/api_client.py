import httpx
from fastapi import HTTPException

class APIClient:
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=10.0)

    async def post(self, url: str, data: dict):
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Service unavailable")
        
    async def get(self, url: str):
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Service unavailable")

api_client = APIClient()  # Create a reusable instance
