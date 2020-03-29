from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    """登录视图"""
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    if not all([user_name, password]):
        resp = {
            "code": 0,
            "message": "empty username or password"
        }
        return jsonify(resp)
    
    if user_name == "zhangsan" and password == "123":
        resp = {
            "code": 1,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "wrong username or password"
        }
        return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)