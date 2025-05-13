from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Insight(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
    