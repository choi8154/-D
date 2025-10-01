from fastapi import FastAPI, BackgroundTasks, APIRouter, Depends
import uvicorn

app = FastAPI()

def write_log(message):
    with open("log.txt", "a") as a:
        a.write(message)

def tsetfunc():
    return "Success Test"

router = APIRouter(
    prefix="/homepage",
    # dependencies = [Depends(tsetfunc)], #!이런식으로 전역으로 사용 하면 저장값을 내부에서 딕셔너리라 생각하고 다루기에 오류가남
    tags=["home"] #! tags는 리스트로
)

@router.get("/")
def get_sub(sub:int=1, test = Depends(tsetfunc)):
    return {"msg":f"This page is {sub}, test : {test}"}

@router.get("/log")
async def read_logs(background_tasks:BackgroundTasks, text:str=None):
    background_tasks.add_task(write_log, f"write_log endpoint was accessed : {text}\n")
    return {"msg":f"{text} recoding is success"}

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)