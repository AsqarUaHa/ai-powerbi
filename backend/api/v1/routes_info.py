from fastapi import APIRouter

from ...schemas.info import ServiceInfoResponse

router = APIRouter()


@router.get("/info", response_model=ServiceInfoResponse)
async def project_info() -> ServiceInfoResponse:
    """Базовая информация о сервисе AI-аналитики и доступных режимах."""
    return ServiceInfoResponse()
