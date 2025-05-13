from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def get_model_metrics():
    return {
        "accuracy": "92.4%",
        "precision": "88.7%",
        "recall": "90.2%"
    }
