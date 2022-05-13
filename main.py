import math
import string
from typing import Optional

from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    element: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

#sum1n
@app.get("/sum1n/{number}")
async def sum_to_n(number: int):
    sum = 0
    for i in range(1,number+1):
        sum = sum + i
    return {"result": sum}

#fibo
@app.get("/fibo")
async def fibo(n: int):
    n0 = 0
    n1 = 1

    if n == 0:
        return {"result": 0}
    elif n == 1:
        return {"result": 1}
    else:
        for i in range (2, n):
            ans = n0 + n1
            n0 = n1
            n1 = ans
        return {"result": ans}

#reverse
@app.post("/reverse")
async def reverse(request: Request):
    string = request.headers.get('string')
    return {"result": string[::-1]}

#list
elements =[]
@app.put("/list")
async def update_list(item: Item):
    elements.append(item.element)
    return {"result": elements}

@app.get("/list")
async def get_list():
    return {"result": elements}

@app.get("/math/{num}")
async def mathematics(num:int):
    root = math.sqrt(num)
    sq = num * num
    return {"root": root, "square": sq}

class Stats(BaseModel):
    count: int
    type: str

finances =[]
@app.post("/fin")
async def finance(stats:Stats):
    if stats.type == "decrease":
        finances.append(-stats.count)
    elif stats.type == "increase":
        finances.append(stats.count)
    
    return {"result": finances}
    

#calculator
@app.post("/calculator")
async def calculator(calculator: str):
    arr = calculator.split(',')
    num1 = int(arr[0])
    num2 = int(arr[2])
    op = arr[1] # arithmetic operation
    result = -1
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = int(num1 / num2)
    else:
       result = 0
    
    return {"result": result}
    

#items
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = "test"):
    #select item_id,name from item where item_id = item_id
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price":item.price}