from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import csv, io, uvicorn
from faker import Faker
from random import randint as rand

faker = Faker("ko-KR")

app = FastAPI()

def csv_streamer():
    # data = [["name", "age"],["alice", 32],["bopb", 29]]
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["name", "age","email","adress"])
    yield output.getvalue()
    output.truncate()
    output.seek(0)
    for _ in range(100):
        data = [faker.name(), rand(10, 40), faker.email(), faker.address()]
        writer.writerow(data)
        yield output.getvalue()
        output.truncate()
        output.seek(0)

@app.get("/csv")
def get_csv():
    return StreamingResponse(
        csv_streamer(),
        headers={"Content-Type": "text/csv"}
    )

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)