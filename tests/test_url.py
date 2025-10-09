import pytest
from app.crud.url import create_url
from app.models.url import URL
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_db

# shorten

def test_shorten(client):
    test_url = "https://google.com/"

    response = client.post("/shorten", json={"original_url": test_url})
    assert response.status_code == 200
    data = response.json()
    assert data["original_url"] == test_url

def test_shorten_rejects_empty_body(client):
    response = client.post("/shorten")
    assert response.status_code == 422 # Unprocessable Entity

def test_shorten_rejects_invalid_url(client):
    test_url = "test"

    response = client.post("/shorten", json={"original_url": test_url})
    assert response.status_code == 422

# get url

def test_get_url(client):
    test_url = "https://google.com/"
    response = client.post("/shorten", json={"original_url": test_url})
    data = response.json()
    short_url = data["short_url"]

    response = client.get(f"/{short_url}", follow_redirects=False)
    assert response.status_code == 307 # Temporary redirect
    assert response.headers["Location"] == test_url

def test_get_invalid_url(client):
    response = client.get("/test}", follow_redirects=False)
    assert response.status_code == 404

# url info

def test_get_url_info(client):
    test_url = "https://google.com/"
    response = client.post("/shorten", json={"original_url": test_url})
    data = response.json()
    short_url = data["short_url"]

    response = client.get(f"/{short_url}/info")
    assert response.status_code == 200
    data = response.json()
    assert data["short_url"] == short_url
    assert data["original_url"] == test_url
    assert data["clicks"] == 0

def test_get_invalid_url_info(client):
    response = client.get("/test/info")
    assert response.status_code == 404

def test_url_clicks(client):
    test_url = "https://google.com/"
    response = client.post("/shorten", json={"original_url": test_url})
    data = response.json()
    short_url = data["short_url"]

    client.get(f"/{short_url}", follow_redirects=False)
    client.get(f"/{short_url}", follow_redirects=False)

    response = client.get(f"/{short_url}/info")
    data = response.json()
    assert data["clicks"] == 2
