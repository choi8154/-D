from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    data: str

@app.get("/", response_model=List[Item])
def read_items():
    datas = [{"id": 1, "data": "flask", "password":"1234"},{"id": 2, "data": "fastAPI", "password":"1234"}]
    return datas