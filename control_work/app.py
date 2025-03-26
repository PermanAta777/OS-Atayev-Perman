from fastapi import FastAPI, HTTPException
from fibonacci import FibonacciGenerator
from palindrome import PalindromeChecker
from linked_list import LinkedList
from pydantic import BaseModel

app = FastAPI()

class ListInput(BaseModel):
    values: List[int]

@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    try:
        return {"result": FibonacciGenerator.generate_fibonacci(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/palindrome/{number}")
def check_palindrome(number: int):
    try:
        return {"is_palindrome": PalindromeChecker.is_palindrome(number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/reverse_list")
def reverse_list(input: ListInput):
    try:
        ll = LinkedList()
        for value in input.values:
            ll.append(value)
        ll.reverse()
        return {"result": ll.to_list()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
