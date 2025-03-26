import pytest
import httpx
from src.server import app

@pytest.mark.asyncio
async def test_fibonacci():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/fibonacci/5")
        assert response.status_code == 200
        assert response.json()["result"] == [0, 1, 1, 2, 3]

@pytest.mark.asyncio
async def test_fibonacci_invalid():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/fibonacci/-1")
        assert response.status_code == 400

@pytest.mark.asyncio
async def test_palindrome():
    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/palindrome", json={"number": 121})
        assert response.status_code == 200
        assert response.json()["is_palindrome"] == True
