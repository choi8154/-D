from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
#response_medel(응답모델)을 사용한 유효성 검사.
app = FastAPI()

class Cat(BaseModel):
    name : str

class Dog(BaseModel):
    name : str

@app.get("/item/", response_model=Union[Cat,Dog])
async def read_item(animal):
    if animal == "cat":
        return {"name":"nabi"}
    if animal == "dog":
        return {"name":"mungmui"}