from fastapi import APIRouter
from datetime import datetime
from .models import Insight

router = APIRouter()

# Fake in-memory database
insights_db = [Insight(id=1, title="AI is Transforming Startups", description ="Startups are leveraging AI to automate workflows."),
                Insight(id=2, title="Microservices with FastAPI", descripion =" maintainable.")]

@router.get("/insights", response_model=list[Insight])
def get_insights():
    return insights_db

@router.post("/insights", response_model=Insight)
def create_insight(insight: Insight):
    insights_db.append(insight)
    return insight
    