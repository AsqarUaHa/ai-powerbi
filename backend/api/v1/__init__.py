from fastapi import APIRouter

from .routes_health import router as health_router
from .routes_info import router as info_router
from .routes_auth import router as auth_router
from .routes_dashboards import router as dashboards_router
from .routes_analyze import router as analyze_router
from .routes_history import router as history_router
from .routes_export import router as export_router

router = APIRouter()

# Базовые технические эндпоинты
router.include_router(health_router, tags=["health"])
router.include_router(info_router, prefix="/info", tags=["info"])

# Бизнес-функциональность
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(dashboards_router, prefix="/dashboards", tags=["dashboards"])
router.include_router(analyze_router, prefix="/analyze", tags=["analysis"])
router.include_router(history_router, prefix="/history", tags=["history"])
router.include_router(export_router, prefix="/export", tags=["export"])
