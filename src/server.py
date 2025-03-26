from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.fibonacci import FibonacciGenerator
from src.palindrome import PalindromeChecker

app = FastAPI()

class NumberInput(BaseModel):
    number: int

@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    try:
        return {"result": FibonacciGenerator.generate(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/palindrome")
async def check_palindrome(input: NumberInput):
    try:
        return {"is_palindrome": PalindromeChecker.is_palindrome(input.number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
