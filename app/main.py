from fastapi import FastAPI
from app.db import engine
from app.db import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return "Hello World"