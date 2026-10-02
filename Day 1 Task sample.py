#!pip install fastapi
#!pip install uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello Welcome to FastAPI! Day 1 Task"}