import httpx
import asyncio
from loguru import logger

async def fetch_data(url: str, method: str = "GET", data: dict = None, headers: dict = None):
    """Handles async API requests with retries for multiple HTTP methods."""
    
    max_retries = 3  
    retry_delay = 2  
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        for attempt in range(1, max_retries + 1):
            try:
                if method == "GET":
                    response = await client.get(url, headers=headers)
                elif method == "POST":
                    response = await client.post(url, json=data, headers=headers)
                elif method == "PUT":
                    response = await client.put(url, json=data, headers=headers)
                elif method == "DELETE":
                    response = await client.delete(url, headers=headers)
                elif method == "PATCH":
                    response = await client.patch(url, json=data, headers=headers)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")

                response.raise_for_status()  
                return response.json()

            except httpx.RequestError as e:
                logger.warning(f"Request error to {url} (Attempt {attempt}/{max_retries}): {e}")
                
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error {e.response.status_code} from {url}: {e}")
                
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    raise

            if attempt < max_retries:
                await asyncio.sleep(retry_delay)  

    logger.error(f"Failed to reach {url} after {max_retries} attempts")
    raise httpx.HTTPStatusError("Service Unavailable", request=None, response=None)
