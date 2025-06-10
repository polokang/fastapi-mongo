from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
from datetime import datetime
from bson import ObjectId

class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, handler):
        if not ObjectId.is_valid(str(v)):
            raise ValueError("Invalid ObjectId")
        return str(v)

class DatalogData30Min(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    UnitId: int
    DateLogged: datetime
    DateLoggedString: str
    DateCreated: datetime
    DateCreatedString: str
    data: Dict[str, Any]
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            ObjectId: str
        }
        populate_by_name = True 