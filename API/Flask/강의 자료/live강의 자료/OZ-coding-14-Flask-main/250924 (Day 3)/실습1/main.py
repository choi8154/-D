from flask import Flask, jsonify, request
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import os

app = Flask(__name__)
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
# ==================db====================



# ========================================


@app.route("/todos", methods=["GET"])
def get_all_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id":t.id, "task":t.task} for t in todos])


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    db.close()
    if not todo:
        return jsonify({"error": "할 일이 없습니다"}), 404
    return jsonify({"id": todo.id, "task": todo.task})

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    db = SessionLocal()
    new_todo = Todo(task=data["task"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo) # commit 이후 자동 생성된 id 불러오기 위해 세팅
    db.close()
    return jsonify({"id": new_todo.id, "task":new_todo.task}), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"]) #입력할 값이 없어서 이렇게 한거임
def update_todos(todo_id):
    data = request.get_json()
    db = SessionLocal()

    # db에서 항목 찾기
    todo = db.query(Todo).get(todo_id)
    if not todo: # 못찾으면 db닫고 404 반환
        db.close()
        return jsonify({"error":"할 일이 없습니다."}), 404

    # 데이터가 있으면 업데이트ㅁㅈ
    todo.task = data["task"]
    db.commit()

    # 업데이트 된 정보
    updated = {"id":todo.id, "task": todo.task}
    db.close()

    # 업데이트 된 정보
    return jsonify(updated)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    db = SessionLocal()

    # db에서 항목 찾기
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({"error":"할 일이 없습니다."}), 404
    db.delete(todo)
    db.commit()
    db.close()
    return jsonify({"delete":"삭제 완료"}),200


# 400-> bad request: 코딩 잘못
# 401-> 인증: 사이트에 로그인 안했는데 뭔가 하려고해서.. 로그인, 회원가입, #
# 403-> 권한: 사이트에 이미 로그인 한 상태에서 권한이 없는거 # 
# 404 -> 못찾음
# 409-> conflict: 회원가입을 이미 했는데, 또 하는 경


# 200 →> ok
# 201-> Created: 내가 뭘 만들었다. 없는데 만들었다.
# 204-> no content: 뭔가 성공을 하긴 했는데 딱히 응답할거 없을때
if __name__=="__main__":
    app.run(debug=True)