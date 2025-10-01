from fastapi import FastAPI, Query
from typing import List, Dict #고급 타입 힌트를 위한 라이브러리

app = FastAPI()

#?타입 힌트 : 파이썬의 명시적인 힌트와 다르게 호출시 요청이 거부됨
#타입 힌트 경로 매개변수 예제
@app.get('/items/{item_id}')
def read_item(item_id:int):
    return {'item_id':item_id}

#쿼리 매개변수 예제
@app.get('/getdata/')
def read_item(data: str = "funcoding"):
    return {"data":data}


#?고급 타입 힌트 : 
# List 데이터 타입을 쿼리 매개변수로 받는 라우트 예제
@app.get('/items/')
def read_item(q: List[int] = Query([])):
    return {'q': q}
#사용법

# Dict 데이터 타입을 요청 바디로 받는 라우트 예제
@app.post('/create-item/')
def create_item(item: Dict[str, int]):
    return item
#사용법 :  curl 'http://127.0.0.1:8000/create-item/' H "accept : application/json" -H "content-Type:application/json" -d "{\"name\": 2}"