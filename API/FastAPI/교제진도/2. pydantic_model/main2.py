from fastapi import FastAPI
from pydantic import BaseModel, Field #?필드 제약조건
from typing import Optional, List

app = FastAPI()

# ?필드 제약조건: Pydantic 모델에서 필드에 추가적인 정보다 제약 조건을 지정할 수 있는 함수.
class Item(BaseModel):
    # name은 최소 2자, 최대 50자를 가져야 하며 필수 필드
    name:str = Field(...,title="Item Name", min_length=2, max_length=50)
    # description은 선택 필드이며, 최대 300자까지 가능
    description:str = Field(None, description="The description of the item", max_length=300)
    # price는 0보다 커야 하며 필수 필드
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    # tag필드는 선택적이며, 기본값으로 빈 리스트를 갖고, json에서는 item-tags로 나타냄
    tag: List[str] = Field(default=[], alias="item-tags")

@app.post("/items/")
def read_item(item:Item):
    return {"item":item.dict()}

# ?curl Test
'''
curl -X POST "http://127.0.0.1:8000/items/" \
-H "accept:application/json" \
-H "Content-Type: application/json" \
-d '{"name":"myitem", "price":35.3}'
'''