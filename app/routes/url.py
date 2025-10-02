from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.schemas.url import CreateUrlRequest, CreateUrlResponse, GetUrlInfoResponse
from datetime import datetime

router = APIRouter(tags=["URL"])

@router.post("/shorten")
def shorten_url(request: CreateUrlRequest):
    return CreateUrlResponse(id=1, original_url=request.original_url, short_url="test")

@router.get("/{short_url}")
def redirect(short_url: str):
    return RedirectResponse(url="https://www.google.com")

@router.get("/{short_url}/info")
def get_url_info(short_url: str):
    return GetUrlInfoResponse(original_url="https://www.google.com", short_url=short_url, clicks=0, created_at=datetime.now())  



