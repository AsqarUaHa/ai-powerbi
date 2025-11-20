from typing import Optional

from pydantic import BaseModel


class DashboardRead(BaseModel):
    id: int
    powerbi_id: str
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    page_count: int | None = None


class DashboardPageRead(BaseModel):
    id: str
    name: str
    order: int
