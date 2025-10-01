import threading
from flask import Flask
from flask_sock import Sock
import time

app = Flask(__name__)
sock = Sock(app)

# 연결된 클라이언트 보관소
connections = []

@sock.route("/ws")
def websocket(ws):
    connections.append(ws)
    while True:
        data = ws.receive()
        if data is None:
            break
        connections.remove(ws)

def background_jobs():
    while True:
        time.sleep(5)
        for ws in connections:
            try:
                ws.send("서버에서 메세지를 보내고 있습니다.")
            except Exception:
                pass

threading.Thread(target=background_jobs, daemon=True).start() #쓰레드 세팅



if __name__=="__main__":
    app.run(debug=True)