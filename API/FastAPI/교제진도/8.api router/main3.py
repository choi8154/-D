from fastapi import FastAPI, APIRouter, Depends, HTTPException
import uvicorn

app = FastAPI()

def check_token(token: str):
    if token != "my-secret-token":
        raise HTTPException(status_code=404, detail="Unauthorized")
    return token

router = APIRouter(dependencies=[Depends(check_token)])

@router.get("/items")
def get_items():
    return {"message":"Access granted, you can view the items"}

@app.get("/public")
def get_public():
    return {"massage":"This is apublic endpoint"}

app.include_router(router, prefix="/api")

if __name__=="__main__":
    uvicorn.run("main3:app", host="127.0.0.1", port=8000, reload=True)