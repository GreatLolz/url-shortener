from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base
from datetime import datetime

class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True)
    original_url = Column(String)
    short_url = Column(String, unique=True)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now())
