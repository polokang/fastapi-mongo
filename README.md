# FastAPI MongoDB Demo

这是一个使用 FastAPI 和 MongoDB 的示例项目。

## 环境要求

- Python 3.8+
- MongoDB

## 安装

1. 克隆项目
2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置

1. 复制 `.env.example` 到 `.env`
2. 在 `.env` 文件中配置数据库连接信息

## 运行

```bash
python -m uvicorn app.main:app --reload
```

## API 文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 端点

- GET /api/v1/datalog/{unit_id} - 根据 UnitId 查询数据 