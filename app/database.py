from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from .config import get_settings

class Database:
    client: Optional[AsyncIOMotorClient] = None
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