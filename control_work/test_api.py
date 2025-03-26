from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_fibonacci_api():
    response = client.get("/fibonacci/5")
    assert response.status_code == 200
    assert response.json() == {"result": [0, 1, 1, 2, 3]}

def test_palindrome_api():
    response = client.get("/palindrome/121")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": True}

def test_reverse_list_api():
    response = client.post("/reverse_list", json={"values": [1, 2, 3]})
    assert response.status_code == 200
    assert response.json() == {"result": [3, 2, 1]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
