from fastapi import APIRouter

from ...schemas.dashboards import DashboardRead, DashboardPageRead

router = APIRouter()


@router.get("/", response_model=list[DashboardRead])
async def list_dashboards() -> list[DashboardRead]:
    """Список доступных дашбордов (пока статический список по ТЗ)."""
    topics = [
        "Продажи",
        "Логистика",
        "Закупки",
        "Финансы",
        "HR/Персонал",
        "Производство",
        "Маркетинг",
        "Складской учет",
        "Клиентская аналитика",
        "Бюджетирование",
        "Операционная эффективность",
    ]
    return [
        DashboardRead(
            id=i + 1,
            powerbi_id=f"report-{i+1}",
            name=topic,
            category=topic,
            page_count=8,
        )
        for i, topic in enumerate(topics)
    ]


@router.get("/{dashboard_id}", response_model=DashboardRead)
async def get_dashboard(dashboard_id: int) -> DashboardRead:
    """Детали дашборда (демо-ответ)."""
    return DashboardRead(
        id=dashboard_id,
        powerbi_id=f"report-{dashboard_id}",
        name=f"Дашборд #{dashboard_id}",
        category="Демо",
        page_count=8,
        description="Демо-описание дашборда",
    )


@router.get("/{dashboard_id}/pages", response_model=list[DashboardPageRead])
async def list_dashboard_pages(dashboard_id: int) -> list[DashboardPageRead]:
    """Список листов дашборда (пока статический список)."""
    return [
        DashboardPageRead(id=str(i + 1), name=f"Страница {i+1}", order=i)
        for i in range(4)
    ]


@router.post("/sync")
async def sync_dashboards() -> dict:
    """Синхронизация метаданных дашбордов с Power BI (пока заглушка)."""
    return {"status": "scheduled"}
