from flask import Flask, jsonify, request

app = Flask(__name__)

todos = {
    1: "flask 공부하기",
    2: "python 공부하기"
}


@app.route("/todos", methods=["GET"])
def get_all_todos():
    return jsonify(todos)

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    task = todos.get(todo_id)
    if not task:
        return jsonify({"error": "할 일이 없습니다"}), 404
    return jsonify({todo_id: task})

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_id = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data["task"]
    return jsonify({new_id: todos[new_id]}), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"]) #입력할 값이 없어서 이렇게 한거임
def update_todos(todo_id):
    if todo_id not in todos:
        return jsonify({"error":"할 일이 없습니다."}), 404
    data = request.get_json()
    todos[todo_id] = data["task"]
    return jsonify(todos)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    if todo_id not in todos:
        return jsonify({"error":"할 일이 없습니다."}), 404
    delete = todos.pop(todo_id)
    return jsonify({"delete":delete}),200


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