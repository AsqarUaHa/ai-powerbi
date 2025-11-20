from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Pagination(BaseModel):
    page: int = 1
    page_size: int = 20


class Timestamped(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
