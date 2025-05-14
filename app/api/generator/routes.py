from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Optional
from faker import Faker
import random

router = APIRouter()
faker = Faker()

class GenerationRequest(BaseModel):
    data_type: str
    min_count: int
    max_count: int

@router.api_route("/generate", methods=["GET", "POST"])
async def generate_data(request: Request):
    if request.method == "POST":
        body = await request.json()
        req = GenerationRequest(**body)

        # Pick a random number of records to generate between min and max
        count = random.randint(req.min_count, req.max_count)

        # Generate synthetic data based on data_type
        if req.data_type == "text":
            data = [faker.sentence() for _ in range(count)]
        elif req.data_type == "name":
            data = [faker.name() for _ in range(count)]
        elif req.data_type == "email":
            data = [faker.email() for _ in range(count)]
        elif req.data_type == "address":
            data = [faker.address() for _ in range(count)]
        else:
            return {
                "error": f"Unsupported data_type: {req.data_type}. Supported types: text, name, email, address"
            }

        return {
            "message": f"Synthetic {req.data_type} data generated.",
            "count": count,
            "data": data
        }
    else:
        return {
            "message": "This is the synthetic data generator endpoint.",
            "usage": "Send a POST request with data_type, min_count, and max_count in JSON.",
            "example": {
                "data_type": "text",
                "min_count": 5,
                "max_count": 15
            }
        }


# class GenerationRequest(BaseModel):
#     data_type: str
#     min_count: int
#     max_count: int

# @router.api_route("/generate", methods=["GET", "POST"])
# async def generate_data(request: Request):
#     if request.method == "POST":
#         body = await request.json()
#         req = GenerationRequest(**body)
#         return {
#             "message": f"Synthetic {req.data_type} data generation started.",
#             "min": req.min_count,
#             "max": req.max_count
#         }
#     else:  
#         return {
#             "message": "This is the synthetic data generator endpoint.",
#             "usage": "Send a POST request with data_type, min_count, and max_count in JSON."
#         }
