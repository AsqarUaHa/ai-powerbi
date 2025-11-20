from typing import List

from pydantic import BaseModel


class ServiceInfoResponse(BaseModel):
    """Информация о сервисе и доступных режимах анализа."""

    name: str = "PowerBI AI Analytics"
    description: str = (
        "Интеллектуальная система аналитики дашбордов Power BI "
        "с поддержкой текстового и визуального анализа."
    )
    modes: List[str] = [
        "question",  # анализ по вопросу
        "free_form",  # свободный анализ дашборда
        "image",  # анализ изображения графика
    ]
    version: str = "0.1.0"
