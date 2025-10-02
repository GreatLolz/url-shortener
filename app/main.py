from fastapi import FastAPI
from app.db import engine
from app.db import Base
from app.routes import url
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(url.router)