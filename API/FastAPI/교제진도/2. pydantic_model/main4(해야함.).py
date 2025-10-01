from fastapi import FastAPI
from typing import Optional,  List, Union
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    tags: List[str]
    variant: Union[int, str]

    