from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):#1. 클라이언트가 보낸 body의 속성은 기본적으로 JSON(dict)형태임. 그 데이터를 객체화 시켜서
    name: str
    price: float
    is_offer: bool = None

@app.post('/items/') 
def read(item:Item):
    return {"item": item.dict()} #2. 이런식으로 item의 형식을 변환하여 받을 수 있도록함.(파싱)



# ?왜 Pydantic BaseModel을 쓰냐?
# 단순히 가독성 때문만은 아니고, 데이터 관리 + 검증 + 문서화까지 한 번에 해결하려고 쓰는 거야.
# 가독성: 여러 필드를 한눈에 보기 쉽게 클래스 안에 모아둠.
# 재사용성: 라우트마다 일일이 param1, param2, ... 붙이면 중복 폭발 → 모델에 모아두면 다른 라우트에서도 그대로 재사용 가능.
# 자동 검증: 타입 힌트 기반으로 잘못된 타입이 들어오면 자동으로 에러 반환 (예: age: int에 "스물셋" 넣으면 422 에러).
# 자동 문서화: FastAPI가 BaseModel 정의만 보고 OpenAPI 스펙 문서(/docs) 자동 생성.

#? Curl Test
'''
curl -X POST "http://127.0.0.1:8000/items/" \
-H "accept:application/json" -H "Content-Type: application/json" \
-d '{"name":"choi", "price":12.1, "is_offer":true}'
'''