from fastapi import FastAPI, APIRouter
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

# ?미들웨어 + teg : 미들웨어는 요청과 응답 사이에 작업을 넣는 것.
app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "localhost", "127.0.0.1"]
)

router = APIRouter()

@router.get("/items/")
def read_item():
    return {"msg":"Hello,Middleware"}

app.include_router(router, prefix="/api", tags=["items"])

@app.get("/hello")
def read_item():
    return {"msg":"Hello World"}

if __name__=="__main__":
    uvicorn.run("main2:app", host="127.0.0.1",port=8000, reload=True)