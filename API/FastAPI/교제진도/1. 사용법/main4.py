from fastapi import FastAPI
from typing import Optional, Union, Callable, Iterable, Sequence

app = FastAPI()

@app.get('/')
def read_item():
    return {"massage":"Hello, FastAPI"}

@app.get('/items/{item_id}')
def read_item(item:int)->dict:
    return {"item": item}

@app.get('/items/')
def read_item(skip: int=0, limit: str=0):
    return {"skip":skip, "limit":limit}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id":item_id, "item":item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"massage": f"Item {item_id} has been deleted"}