from fastapi import FastAPI, APIRouter, Depends, HTTPException
import uvicorn

app = FastAPI()

def common_depends():
    return "This is common depends"

parent_router = APIRouter(
    prefix='/parent',
    tags=['parent'],
    dependencies=[Depends(common_depends)])

@parent_router.get("/items")
def get_items():
    return {"massage":"This is an item from the parent router"}

child_router = APIRouter()

@child_router.get('/items')
def get_child(common: str = Depends(common_depends)):
    return {"massage":"This is an item from the child router", "common":common}

parent_router.include_router(child_router, prefix="/child")

app.include_router(parent_router)

if __name__=="__main__":
    uvicorn.run("main4:app", host="127.0.0.1", port=8000, reload=True)