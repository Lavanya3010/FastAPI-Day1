#!pip install fastapi uvicorn
from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Day 1 Task"}