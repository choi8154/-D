from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app=FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/user')
def read_root(request:Request, username:str = "jhon"):
    return templates.TemplateResponse("index.html", {"request": request, "username": username})




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)