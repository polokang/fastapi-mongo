from fastapi import APIRouter, HTTPException
from typing import List
from ..models import DatalogData30Min
from ..database import Database
from pymongo.errors import ServerSelectionTimeoutError
from bson import ObjectId
from datetime import datetime
import time

router = APIRouter()

@router.get("/datalog/{unit_id}", response_model=List[DatalogData30Min])
async def get_datalog_by_unit_id(
    unit_id: str,
    start_date: str = "2025-06-01",
    end_date: str = "2025-06-10"
):
    try:
        # 检查数据库连接
        db = Database.get_db()
        # 尝试执行一个简单的命令来验证连接
        await db.command('ping')
        
        # 将 unit_id 转换为 int64
        unit_id_int = int(unit_id)
        
        # 将日期字符串转换为 Unix 时间戳
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
        start_unix = int(time.mktime(start_datetime.timetuple()))
        end_unix = int(time.mktime(end_datetime.timetuple()))
        
        # 构建查询条件
        query = {
            "UnitId": unit_id_int,
            "DateLoggedUnix": {
                "$gte": start_unix,
                "$lte": end_unix
            }
        }
        
        # 执行查询
        cursor = db.DatalogData30Min.find(query)
        results = await cursor.to_list(length=None)  # 不限制返回数量
        
        if not results:
            raise HTTPException(
                status_code=404, 
                detail=f"No data found for UnitId: {unit_id} between {start_date} and {end_date}"
            )
        
        # 处理每条记录
        processed_results = []
        for result in results:
            # 将 ObjectId 转换为字符串
            result["_id"] = str(result["_id"])
            
            # 构造返回数据
            processed_results.append({
                "UnitId": result["UnitId"],
                "DateLogged": result["DateLogged"],
                "DateLoggedString": result["DateLoggedString"],
                "DateCreated": result["DateCreated"],
                "DateCreatedString": result["DateCreatedString"],
                "data": {k: v for k, v in result.items() if k not in ["UnitId", "DateLogged", "DateLoggedString", "DateCreated", "DateCreatedString"]}
            })
            
        return processed_results
    except ServerSelectionTimeoutError:
        raise HTTPException(
            status_code=503,
            detail="无法连接到数据库，请检查数据库连接配置和网络状态"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid input: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 