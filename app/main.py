# app/main.py
from fastapi import FastAPI
from app.api.insights.routes import router as insights_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastIQ, thank you for your help mate !!! you are my Ninja buddy"}

