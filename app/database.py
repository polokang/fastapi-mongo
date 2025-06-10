from typing import Optional, Any
from .config import get_settings
from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    client: Optional[Any] = None
    settings = get_settings()
    
    @classmethod
    async def connect_db(cls):
        cls.client = AsyncIOMotorClient(cls.settings.mongodb_url)
        
    @classmethod
    async def close_db(cls):
        if cls.client is not None:
            cls.client.close()
            
    @classmethod
    def get_db(cls):
        return cls.client[cls.settings.database_name] 