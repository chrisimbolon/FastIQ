from fastapi import APIRouter
from datetime import datetime
from .models import Insight

router = APIRouter()

# Fake in-memory database
insights_db = []

@router.get("/insights", response_model=list[Insight])
def get_insights():
    return insights_db

@router.post("/insights", response_model=Insight)
def create_insight(insight: Insight):
    insights_db.append(insight)
    return insight
    