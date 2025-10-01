from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()

router = APIRouter()


@router.get("/items/")
def read_item():
    return {"msg":"hello,world"}

@router.get("/users/")
def read_user():
    return {"user":"choi"}

if __name__=="__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload=True)

app.include_router(router, prefix="/api/v1", tags=["items"])
