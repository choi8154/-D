from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# ?쿼리 클래스 : Query(defult, 옵션들)

app = FastAPI()

# ge(greater than or equal to) : 숫자 이상
# le(less than or equal to) : 숫자 이하
@app.get("/items/", response_class=HTMLResponse)
def read_item(page:int = Query(1.0, ge=1, le=50.0)):
    return f"<h1>{page}번째 페이지 입니다.</h1>"

# alias : 매개변수의 별칭을 지정하여 함수의 매개변수와 사용자가 URL로 요청하는 매개변수의 이름을 다르게함.
@app.get("/alias/")
def read_alias(secret_parameter:str = Query(alias="query")):
    return {"secret_parameter":secret_parameter}
# 실행 : curl "http://127.0.0.1:8000/alias/?query=query"
# 결과 : {"secret_parameter":"query"}%

# deprecated : API의 변경 사항을 관리 할 수 있게 해줌. deprecated=True 를 하여 해당 매개변수는 향후 사용하지 말 것을 권장하는 신호를 보냄
@app.get("/deprecated")
def read_deprecated(q:str = Query(None, deprecated=True)):
    return {"q":q} # 클라이언트는 q라는 쿼리 매개변수를 정송할 수 있으나 곧 지원되지 않을 예정임을 명시함.

# description : 쿼리 매개변수에 대한 상세한 설명을 추가할 수 있음.
@app.get("/info")
def read_info(info:str = Query(None, description="정보를 입력해 주세요.")):
    return {"info":info}