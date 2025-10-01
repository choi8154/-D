from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template("typing.html")

@sock.route("/ws")
def websocket(ws):
    # 타이핑 중입니다 / 메시지 안나오게 처리
    while True:
        data = ws.receive()
        if data == "typing":
            ws.send("입력 중입니다.")
        elif data == "stop":
            ws.send("")

        if data is None: # 연결 종료
            break


if __name__ == "__main__":
    app.run(debug=True)