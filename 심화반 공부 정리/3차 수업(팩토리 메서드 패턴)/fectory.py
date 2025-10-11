from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

app = FastAPI()

DB_URL = "mysql+mypysql://root:dain8154@localhost/dbname"

engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

class UserCreate(BaseModel):
    name: str
    age: int

Base.metadata.create_all(bind=engine)

@app.post("/Users/")
def create_user():
    pass