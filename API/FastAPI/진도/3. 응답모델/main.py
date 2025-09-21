from fastapi import FastAPI
from pydantic import BaseModel
#?응답모델이란?
# 클라이언트에 반환되는 데이터의 구조를 정의하는 데 사용되는 강력한 기능.

# 시리얼라이즈:데이터를 일련의 비트로 변환하여 
# 파일, 메모라, 네트워크를 통해 저장하거나 전송할 수 있는 형식을 말함.


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float

def get_item_from_db(id):
    # 매우 간단한 아이템 반환
    return {"name":"Simple Item", "description":"A item description"
            ,"price": 50.0, "dis_price": 45.0}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item_from_db(item_id)
    return item