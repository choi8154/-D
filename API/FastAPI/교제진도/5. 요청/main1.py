from fastapi import FastAPI, Body
# ?요청 바디
app = FastAPI()

@app.post("/item/")
def create_item(item:dict = Body(...)):
    return {"item":item}
# 실행
'''
curl -X POST "http://127.0.0.1:8000/item/" \
-H "accept:application/json" \
-H "Content-Type: application/json" \
-d '{"key":"value"}'
'''
# 결과 : {"item":{"key":"value"}}%

# 여러가지 옵션들
@app.post("/items/")
def create_item(item:dict = Body(None, example={"key":"Value"}, media_type="application/json", alias="tiem_alias", title="Sample Item", description="this is a sample item", deprecated=False)):
    return {"item":item}
# http://127.0.0.1:8000/items/docs 에서 상태 확인 가능.