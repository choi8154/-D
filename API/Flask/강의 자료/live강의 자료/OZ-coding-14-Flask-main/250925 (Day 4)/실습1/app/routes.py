from flask import Flask, request, jsonify, Blueprint
from .models import SessionLocal, Todo

todo_bp = Blueprint("todo", __name__)


@todo_bp.route("/todos", methods=["GET"])
def get_all_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id":t.id, "task":t.task} for t in todos])


@todo_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    db.close()
    if not todo:
        return jsonify({"error": "할 일이 없습니다"}), 404
    return jsonify({"id": todo.id, "task": todo.task})

@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    db = SessionLocal()
    new_todo = Todo(task=data["task"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo) # commit 이후 자동 생성된 id 불러오기 위해 세팅
    db.close()
    return jsonify({"id": new_todo.id, "task":new_todo.task}), 201

@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"]) #입력할 값이 없어서 이렇게 한거임
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


@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
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
