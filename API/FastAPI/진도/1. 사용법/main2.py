from fastapi import FastAPI

app = FastAPI()
# 경로 매개변수를 적용시킨 라우트
# 경로 매개변수 : URL특정 부분을 변수로써 사용햐여 동적으로 변할 수 있눈 겂울 처리할 때 사용.
@app.get('/items/{item_id}')
def read_item(item_id):
    return {"item_id": item_id}

#경로 매개변수가 2개인 경우
@app.get('/user/{user_id}/items/{item_id}')# 경로 매개변수 : URL특정 부분을 변수로써 사용햐여 동적으로 변할 수 있눈 겂울 처리할 때 사용.
def read_item(user_id, item_id):
    return {"user_id": user_id, "item_id": item_id}

#쿼리 매개변수(기본값 X)
# 쿼리 매개변수 : URL의 경로 이후 ?로 시작되는 부분에 정의, 키-값 쌍의 형태로 정보를 전달하는데 사용.
@app.get('/items/off/')
def read_items(skip, limit):
    return {"skip":skip, "limit":limit}
# http://127.0.0.1:8000/items/off/?skip=5&limit=10 형식으로 사용

#쿼리 매개변수(기본값 O)
@app.get('/items/on/')
def read_items(skip=1, limit=1):
    return {"skip":skip, "limit":limit}
# http://127.0.0.1:8000/items/on/ 형식으로 사용해도 쿼리 매개변수 기본값 반환

# 다른 터미널을 열어 curl 테스팅 하기
# curl "http://127.0.0.1:8000/items/on/?skip=10&limit=10"