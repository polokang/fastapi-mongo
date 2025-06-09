from fastapi import APIRouter, HTTPException
from typing import List
from ..models import DatalogData30Min
from ..database import Database

router = APIRouter()

@router.get("/datalog/{unit_id}", response_model=List[DatalogData30Min])
async def get_datalog_by_unit_id(unit_id: str):
    try:
        db = Database.get_db()
        cursor = db.DatalogData30Min.find({"UnitId": unit_id})
        results = await cursor.to_list(length=None)
        
        if not results:
            raise HTTPException(status_code=404, detail=f"No data found for UnitId: {unit_id}")
            
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 