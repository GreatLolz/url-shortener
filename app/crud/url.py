import string
import random
from pydantic.networks import HttpUrl
from sqlalchemy.orm import Session
from app.models.url import URL

def generate_short_url(length: int = 5):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    return short_url

def create_url(db: Session, original_url: HttpUrl) -> URL:
    short_url = generate_short_url()

    while db.query(URL).filter(URL.short_url == short_url).first():
        short_url = generate_short_url()

    obj = URL(original_url=str(original_url), short_url=short_url)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_url(db: Session, short_url: str) -> URL | None:
    return db.query(URL).filter(URL.short_url == short_url).first()

def update_clicks(db: Session, short_url: str):
    url = db.query(URL).filter(URL.short_url == short_url).first()
    url.clicks += 1
    db.commit()
    