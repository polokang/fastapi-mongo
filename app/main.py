from fastapi import FastAPI
from .database import Database
from .api.endpoints import router

app = FastAPI(
    title="MongoDB FastAPI Demo",
    description="FastAPI application with MongoDB integration",
    version="1.0.0"
)

# 注册路由
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_db_client():
    await Database.connect_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await Database.close_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 