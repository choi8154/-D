from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse

app = FastAPI()

@app.get("/json", response_class=JSONResponse)
def read_json():
    return {"msg":"This is JSON"}

#?HTML전체나 문서를 반환 할 때 사용. 페이지
@app.get("/html", response_class=HTMLResponse)
def read_html():
    return "<h1 class=choi>이것은 HTML형식이유</h1>"

#?단순 텍스트를 반환 할 때 사용, 로깅메지시나 단순한 안내문구에 사용
@app.get("/text", response_class=PlainTextResponse)
def read_text():
    return "이것은 단지 문자열이여"

#?다른 URL로 리디렉션, 사용자를 다른페이지로 유도할 때 사용
@app.get("/redirect")
def read_redirect():
    return RedirectResponse(url="/html")
#용청 방법 : curl "http://127.0.0.1:8000/redirect" -L << -L은 리디렉션을 따르도록 지시함