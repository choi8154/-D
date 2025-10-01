from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import uvicorn

DB_URL = "mysql+pymysql://root:dain8154@localhost/practice" # 데이터베이스 경로

engine = create_engine(DB_URL, echo=True) # 경로와 연결방식을 저장하여 데이터가 드나들 수 있는 정보(문)을 객체로 생성

Base = declarative_base()

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    login_id = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class UserCreate(BaseModel):
    name : str
    login_id : str
    password : str
    email: str

def get_db():
    db = Session(bind=engine) # 작업 도구가 들어있는 실행자를 engine에 보내서 작업하도록함
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine) # Base에 등록된 모든 테이블(클래스에 따른)을 engine에 등록된 주소와 그 방식으로 만들어줘

@app.get("/")
def read_root():
    return {"msg":"Hello, World!"}

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name = user.name,login_id = user.login_id, password= user.password , email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"id":new_user.id , "name": new_user.name, "login_id": new_user.login_id, "password":new_user.password, "email":new_user.email}

if __name__=="__main__":
    uvicorn.run("main1:app", port=8000, host="127.0.0.1", reload=True)



# 아 그리고 flask랑 다른게 request.get_json()을 써야 post를 제이슨 파일로 받을 수 있던데
# 그리고 request를 엔드포인트에 추가 해야 바디에서 데이터를 받아 올 수 있는거 같던데 
# fastapi는 그냥 엔드포인트 함수에 인수(파라메터)만 추가해주면 얘가 post의 body에 있는 정보로 받는 것 같더라?
#  그러면 만약 엔드포인트에 a라는 파라메터가 있으면 
# get일 때는 ?a=hi 로 받고 
# post일 때는 body에서 온 정보를 받는 역할을 a 가 하는건가?

# ?정답이다 연금술사.