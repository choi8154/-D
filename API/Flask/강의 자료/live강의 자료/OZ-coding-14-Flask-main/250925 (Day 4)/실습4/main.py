from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("btc.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:  # 연결 종료
            print("[WS] client disconnected")  # 로그
            break

        print(f"[WS] recv: {data}")  # 로그

        # 감정 단어 사전
        pos = ["love", "좋아", "행복"]   # 긍정
        neg = ["hate", "죽어", "싫어"]   # 부정

        if any(word in data for word in pos):
            sentiment = "긍정!!"
        elif any(word in data for word in neg):
            sentiment = "부정!!"
        else:
            sentiment = "중립!!"

        print(f"[WS] send: {sentiment}")  # 로그
        try:
            ws.send(sentiment)  # ★ 반드시 보내주기!
        except Exception as e:
            print(f"[WS] send error: {e}")
            break

if __name__ == "__main__":
    app.run(debug=True)