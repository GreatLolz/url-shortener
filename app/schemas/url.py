from pydantic import BaseModel
from datetime import datetime
from pydantic.networks import HttpUrl

class CreateUrlRequest(BaseModel):
    original_url: HttpUrl

class CreateUrlResponse(BaseModel):
    id: int
    original_url: HttpUrl
    short_url: str

class GetUrlInfoResponse(BaseModel):
    original_url: HttpUrl
    short_url: str
    clicks: int
    created_at: datetime
