from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("hello.html", name="흠") # html 파일명, 넘길 변수명과 값

@app.route("/user/<username>")
def user(username):
  return render_template("user.html", username=username)

if __name__ == "__main__":
  app.run(debug=True)