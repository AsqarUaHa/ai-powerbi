from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    """Проверка работоспособности сервиса."""
    return {"status": "ok", "service": "powerbi-ai-analytics"}
