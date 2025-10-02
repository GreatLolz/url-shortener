from pydantic import BaseModel
from datetime import datetime

class CreateUrlRequest(BaseModel):
    original_url: str

class CreateUrlResponse(BaseModel):
    id: int
    original_url: str
    short_url: str

class GetUrlInfoRequest(BaseModel):
    short_url: str

class GetUrlInfoResponse(BaseModel):
    original_url: str
    short_url: str
    clicks: int
    created_at: datetime
