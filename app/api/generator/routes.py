from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class GenerationRequest(BaseModel):
    data_type: str
    min_count: int
    max_count: int

@router.api_route("/generate", methods=["GET", "POST"])
async def generate_data(request: Request):
    if request.method == "POST":
        body = await request.json()
        req = GenerationRequest(**body)
        return {
            "message": f"Synthetic {req.data_type} data generation started.",
            "min": req.min_count,
            "max": req.max_count
        }
    else:  # GET
        return {
            "message": "This is the synthetic data generator endpoint.",
            "usage": "Send a POST request with data_type, min_count, and max_count in JSON."
        }
