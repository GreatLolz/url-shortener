from fastapi import FastAPI
from app.routes import url
app = FastAPI()

app.include_router(url.router)