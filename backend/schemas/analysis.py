from typing import Any, List, Optional

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """Запрос на анализ по вопросу пользователя."""

    question: str
    dashboard_id: Optional[int] = None
    page_id: Optional[str] = None


class DashboardAnalysisRequest(BaseModel):
    """Запрос на свободный анализ конкретного дашборда/листа."""

    dashboard_id: int
    page_id: Optional[str] = None
    focus: Optional[str] = None  # overview/anomalies/correlations/forecast


class TableData(BaseModel):
    """Табличный фрагмент результата анализа."""

    title: str
    columns: List[str]
    rows: List[list[Any]]


class AnalysisResponse(BaseModel):
    """Унифицированный ответ AI-анализа.

    Соответствует требованиям ТЗ: краткий ответ, подробности, тренды, рекомендации и таблицы.
    """

    query_id: Optional[int] = None
    short_answer: str
    detailed_answer: str
    trends: List[str] = []
    recommendations: List[str] = []
    tables: List[TableData] = []
