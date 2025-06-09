from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class DatalogData30Min(BaseModel):
    UnitId: str
    timestamp: datetime
    data: dict[str, Any]
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        } 