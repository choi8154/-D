from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<username>")
def hollo_world(username):
    return render_template("hello.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)