from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import os



# ==================db====================
# db정의
BASE_DIR = os.path.dirname(__file__) # 현재 디렉터리 위치
INSTANCE_DIR = os.path.join(BASE_DIR, "instance") # 현재 디렉터리에 os.path(현재 디랙터리)에 instance를 생성
os.makedirs(INSTANCE_DIR, exist_ok=True) # 

DATABASE_URL = f"sqlite:///{os.path.join(INSTANCE_DIR, "todos.db")}"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
# ==================db====================
# 모델정의
Base = declarative_base()

class Todo(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)

    def __repr__(self):
        return f"<Todo(id={self.id}, task={self.task})>"
    


Base.metadata.create_all(bind=engine)