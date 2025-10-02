from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.schemas.url import CreateUrlRequest, CreateUrlResponse, GetUrlInfoResponse
from app.db import get_db
from app.crud import url as crud
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException

router = APIRouter(tags=["URL"])

@router.post("/shorten", response_model=CreateUrlResponse)
def shorten_url(request: CreateUrlRequest, db: Session = Depends(get_db)):
    obj = crud.create_url(db, request.original_url)
    return obj

@router.get("/{short_url}")
def redirect(short_url: str, db: Session = Depends(get_db)):
    obj = crud.get_url(db, short_url)
    if not obj:
        raise HTTPException(status_code=404, detail="URL not found")
    crud.update_clicks(db, short_url)
    return RedirectResponse(url=obj.original_url)

@router.get("/{short_url}/info", response_model=GetUrlInfoResponse)
def get_url_info(short_url: str, db: Session = Depends(get_db)):
    obj = crud.get_url(db, short_url)
    if not obj:
        raise HTTPException(status_code=404, detail="URL not found")
    return obj  



