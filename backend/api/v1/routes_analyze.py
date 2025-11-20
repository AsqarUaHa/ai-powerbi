from fastapi import APIRouter, Depends, File, UploadFile

from ...schemas.analysis import (
    QuestionRequest,
    DashboardAnalysisRequest,
    AnalysisResponse,
)
from ...services.ai import AIService, get_ai_service

router = APIRouter()


@router.post("/question", response_model=AnalysisResponse)
async def analyze_question(
    payload: QuestionRequest,
    ai: AIService = Depends(get_ai_service),
) -> AnalysisResponse:
    """Режим 1: анализ по текстовому вопросу пользователя."""
    return await ai.analyze_question(payload)


@router.post("/free-form", response_model=AnalysisResponse)
async def analyze_dashboard_free_form(
    payload: DashboardAnalysisRequest,
    ai: AIService = Depends(get_ai_service),
) -> AnalysisResponse:
    """Режим 2: свободный анализ выбранного дашборда/листа."""
    return await ai.analyze_dashboard(payload)


@router.post("/image", response_model=AnalysisResponse)
async def analyze_image(
    file: UploadFile = File(...),
    ai: AIService = Depends(get_ai_service),
) -> AnalysisResponse:
    """Режим 3: анализ изображения графика (скриншот визуализации)."""
    content = await file.read()
    return await ai.analyze_image(file.filename, content)
