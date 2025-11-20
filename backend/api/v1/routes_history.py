from fastapi import APIRouter

from ...schemas.history import QueryRead, InsightCreate, InsightRead

router = APIRouter()


@router.get("/queries", response_model=list[QueryRead])
async def list_queries() -> list[QueryRead]:
    """История запросов (пока возвращает демо-запись)."""
    return [
        QueryRead(
            id=1,
            user_id=1,
            dashboard_id=1,
            query_text="Демо-запрос",
            query_type="question",
        )
    ]


@router.get("/queries/{query_id}", response_model=QueryRead)
async def get_query(query_id: int) -> QueryRead:
    """Детали одного запроса (демо)."""
    return QueryRead(
        id=query_id,
        user_id=1,
        dashboard_id=1,
        query_text="Демо-запрос",
        query_type="question",
    )


@router.post("/insights", response_model=InsightRead)
async def create_insight(payload: InsightCreate) -> InsightRead:
    """Сохранить инсайт (пока без БД)."""
    return InsightRead(
        id=1,
        query_id=payload.query_id,
        user_id=1,
        title=payload.title,
        content=payload.content,
        tags=payload.tags or [],
        is_favorite=True,
    )


@router.get("/insights", response_model=list[InsightRead])
async def list_insights() -> list[InsightRead]:
    """Список сохраненных инсайтов (демо)."""
    return []
