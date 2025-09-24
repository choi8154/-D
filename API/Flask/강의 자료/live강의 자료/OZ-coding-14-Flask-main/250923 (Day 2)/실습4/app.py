from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app) #스웨거를 flask에서 사용하는 방법 apidocs

@app.route("/hello")
def hello():
    """
    Hello API
    ---
    responses:
      200:
        description: 성공 응답
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello, OZ BE14!"
    """
    return jsonify(message="hello, World!")

if __name__=="__main__":
    app.run(debug=True)