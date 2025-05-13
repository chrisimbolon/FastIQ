# app/main.py
from fastapi import FastAPI
from app.api.insights.routes import router as insights_router
from app.api.labeling.routes import router as labeling_router
from app.api.metrics.routes import router as metrics_router
from app.api.generator.routes import router as generator_router

app = FastAPI()

# app.include_router(insights_router)
app.include_router(insights_router, prefix="/insights")
app.include_router(labeling_router, prefix="/labeling")
app.include_router(metrics_router, prefix="/metrics")
app.include_router(generator_router, prefix="/generator")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastIQ, inspired by PhraseIQ"}

