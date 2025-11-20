from fastapi import FastAPI

from api.v1 import router as api_v1_router
from .api.v1.routes_health import router as health_router
from .db.base import Base
from .db.session import engine

app = FastAPI(
    title="PowerBI AI Analytics",
    description="AI-аналитика для дашбордов Power BI",
    version="0.1.0",
)


@app.on_event("startup")
async def on_startup() -> None:
    """Инициализация базы данных при старте приложения.

    Для простоты в дев-среде используем Base.metadata.create_all(). В проде
    рекомендуется управлять схемой через миграции (Alembic).
    """

    Base.metadata.create_all(bind=engine)


# Подключаем роуты
app.include_router(health_router)
app.include_router(api_v1_router, prefix="/api/v1")
