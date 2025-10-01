from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/items/", response_class=HTMLResponse)
def read_item(item:int = Query(...,alias="page")):
    try:
        if item < 0:
            raise ValueError("음수는 허용되지 않습니다.")
        return f"<h1>{item}번째 페이지 입니다.</h1>"
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



#! Qurery는 단일 파라미터에만 뜨일 수 있음. 파이덴딕 모델에는 사용 불가능
#! 대신 파이댄틱 모델에 Field 옵션을 줄 수 있음.