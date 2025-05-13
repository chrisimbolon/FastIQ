from fastapi import APIRouter
from datetime import datetime
from .models import Insight

router = APIRouter()

# Fake in-memory database

from datetime import datetime

insights_db = [
    Insight(id=1, title="AI is Transforming Startups", description="Startups are leveraging AI to automate workflows.", created_at=datetime.utcnow()),
    Insight(id=2, title="Microservices with FastAPI", description="Maintainable.", created_at=datetime.utcnow())
]

@router.get("/insights", response_model=list[Insight])
def get_insights():
    return insights_db

@router.post("/insights", response_model=Insight)
def create_insight(insight: Insight):
    new_id = max(i.id for i in insights_db) + 1 if insights_db else 1
    new_insight = Insight(
        id=new_id,
        title=insight.title,
        description=insight.description,
        created_at=datetime.utcnow()
    )
    insights_db.append(new_insight)
    return new_insight

    