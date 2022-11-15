from typing import Optional
import httpx
from models.AntiTracker_Model import AntiTracker_Model as model

async def catchTracker() -> Optional[model]:
    url = f"https://random-data-api.com/api/v2/banks"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        tracker = model(**data)
        return tracker
