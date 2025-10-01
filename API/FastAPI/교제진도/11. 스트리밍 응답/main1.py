from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from faker import Faker
from random import randint
import time, uvicorn

faker = Faker("ko-KR")

app = FastAPI()

def randdata():
    for i in range(100):
        yield f"{i+1}. 이름 : {faker.name()} | 나이 : {randint(10, 40)} | 주소 : {faker.address()} \n"
        time.sleep(1)

@app.get("/")
def read_data():
    return StreamingResponse(randdata(), media_type="text/plain")

if __name__=="__main__":
    uvicorn.run("main1:app", reload=True, host="127.0.0.1", port=8000)