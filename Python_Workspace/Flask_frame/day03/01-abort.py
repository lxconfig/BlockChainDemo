from flask import Flask, abort, Response


app = Flask(__name__)


@app.route("/login")
def login():
    # 在一些视图函数中，经常要对前端传来的数据进行判断，如:登录视图要判断用户信息
    # 在条件不满足时，可以通过abort()函数来终止视图函数，并返回错误信息给前端
    # 与raise不同的是，abort()函数可以返回错误信息给前端，而不是只给后端
    name, age = "", ""
    if name != 'zhansan' or age != '12':
        # 可以传入标准的HTTP状态码(否则不生效报错)
        abort(404)
        # 还可以传入响应体信息
        # resp = Response("Can't found")
        # abort(resp)

    return 'login success'



if __name__ == "__main__":
    app.run(debug=True)