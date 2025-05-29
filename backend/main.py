from fastapi import FastAPI, Request
from rag_pipeline import get_workout_response
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.post("/ask")
async def ask_ai(request: Request):
    body = await request.json()
    query = body.get("query", "")
    response = get_workout_response(query)
    return {"response": response}

@app.post("/custom-plan")
async def generate_custom(request: Request):
    body = await request.json()
    goal = body.get("goal")
    level = body.get("level")
    plan = get_workout_response(query="", goal=goal, level=level)
    return {"plan": plan}