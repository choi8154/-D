from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/items")
def get_items(skip = random.randint(1,100), limit = random.randint(1,100)):
    return {"skip":skip, "limit":limit}

@app.get("/items/{item:path}")
def get_items(item:str):
    return {"item": item}

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)