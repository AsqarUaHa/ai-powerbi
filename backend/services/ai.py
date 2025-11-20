from __future__ import annotations

from typing import Any

from .typing import AnthropicClient, OpenAIClient
from ..schemas.analysis import (
    QuestionRequest,
    DashboardAnalysisRequest,
    AnalysisResponse,
    TableData,
)


class AIService:
    """Сервис AI-аналитики.

    Сейчас использует заглушки и не ходит во внешние API. В будущем здесь
    будет интеграция с Claude / OpenAI / Gemini и формирование промптов по ТЗ.
    """

    def __init__(
        self,
        anthropic_client: AnthropicClient | None = None,
        openai_client: OpenAIClient | None = None,
    ) -> None:
        self._anthropic = anthropic_client
        self._openai = openai_client

    async def analyze_question(self, payload: QuestionRequest) -> AnalysisResponse:
        """Режим 1: анализ по текстовому вопросу (заглушка)."""

        demo_table = TableData(
            title="Пример сравнения показателей",
            columns=["Показатель", "Значение"],
            rows=[["Продажи Q3", 120000], ["Рост к Q2", "+12%"]],
        )

        return AnalysisResponse(
            query_id=1,
            short_answer="Продажи демонстрируют устойчивый рост, особенно в Q3.",
            detailed_answer=(
                "Это демо-ответ AI. Здесь в будущем будут реальные цифры из Power BI "
                "и развернутый анализ в соответствии с промптом из ТЗ."
            ),
            trends=["Рост продаж в Q3", "Улучшение маржинальности"],
            recommendations=["Сфокусироваться на регионах-лидерах", "Провести анализ причин роста"],
            tables=[demo_table],
        )

    async def analyze_dashboard(self, payload: DashboardAnalysisRequest) -> AnalysisResponse:
        """Режим 2: свободный анализ дашборда (заглушка)."""

        return AnalysisResponse(
            query_id=2,
            short_answer="На дашборде выявлены ключевые тренды и аномалии (демо).",
            detailed_answer=(
                "В будущем здесь будет автоматически сгенерированный обзор дашборда: "
                "ключевые тренды, аномалии, корреляции и прогнозы."
            ),
            trends=["Сезонность спроса", "Аномальный всплеск в октябре"],
            recommendations=["Проверить причины аномалий", "Скорректировать планирование"],
            tables=[],
        )

    async def analyze_image(self, filename: str, content: bytes) -> AnalysisResponse:
        """Режим 3: анализ изображения графика (заглушка)."""

        return AnalysisResponse(
            query_id=3,
            short_answer="График показывает общий восходящий тренд (демо).",
            detailed_answer=(
                "Фактический анализ изображения будет выполнен после интеграции с "
                "мультимодальным AI API (Claude / GPT-4o / Gemini)."
            ),
            trends=["Восходящий тренд", "Легкая волатильность"],
            recommendations=["Проверить устойчивость тренда", "Сравнить с плановыми значениями"],
            tables=[],
        )


def get_ai_service() -> AIService:
    """Фабрика для DI в FastAPI.

    Пока возвращает простую заглушку без внешних клиентов.
    """

    return AIService()
