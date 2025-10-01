from flask import Flask, render_template
from flask_sock import Sock
import requests
import time

app = Flask(__name__)

sock = Sock(app)

@sock.route("/ws")
def websocket(ws):
    while True:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        result = requests.get(url).json()
        price = float(result["price"])
        ws.send(f"비트코인 현재 가격: {price}")
        time.sleep(2)

@app.route("/")
def index():
    return render_template("btc.html")

if __name__ == "__main__":
    app.run(debug=True)