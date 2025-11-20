from fastapi import APIRouter

router = APIRouter()


@router.get("/query/{query_id}/pdf")
async def export_query_pdf(query_id: int) -> dict:
    """Экспорт анализа в PDF (заглушка)."""
    return {"status": "not_implemented", "format": "pdf", "query_id": query_id}


@router.get("/query/{query_id}/csv")
async def export_query_csv(query_id: int) -> dict:
    """Экспорт таблиц в CSV (заглушка)."""
    return {"status": "not_implemented", "format": "csv", "query_id": query_id}
