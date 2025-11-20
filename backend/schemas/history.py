from typing import List, Optional

from pydantic import BaseModel


class QueryRead(BaseModel):
    id: int
    user_id: int
    dashboard_id: Optional[int] = None
    query_text: str
    query_type: str  # 'question', 'free_form', 'image'


class InsightCreate(BaseModel):
    query_id: int
    title: str
    content: str
    tags: Optional[List[str]] = None


class InsightRead(BaseModel):
    id: int
    query_id: int
    user_id: int
    title: str
    content: str
    tags: List[str]
    is_favorite: bool = False
