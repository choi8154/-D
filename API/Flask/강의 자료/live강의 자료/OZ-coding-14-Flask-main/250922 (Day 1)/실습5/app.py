from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    # TODO: index.html 반환


@app.route("/greet")
def greet():
    name = request.args.get("name", default="unknown")
    return render_template("greet.html", name=name)
    # TODO: URL에서 name 값 받아오기
    # name = ???
    # return render_template("greet.html", ???)


if __name__ == "__main__":
    app.run(debug=True)
