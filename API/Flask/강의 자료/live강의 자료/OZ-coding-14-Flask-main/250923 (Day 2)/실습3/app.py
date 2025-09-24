from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/<name>")
def read_item(name):
    return jsonify(massage=f"{name}님, BE14 캠프에 오신 걸 환영합니다!")


if __name__=="__main__":
    app.run(debug=True)