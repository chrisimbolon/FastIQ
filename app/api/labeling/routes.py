from fastapi import APIRouter

router = APIRouter()

@router.get("/progress")
def get_labeling_progress():
    return {
        "text_classification": "85%",
        "image_segmentation": "62%",
    }
