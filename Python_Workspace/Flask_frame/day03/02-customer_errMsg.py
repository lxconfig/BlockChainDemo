from flask import Flask, abort, Response


app = Flask(__name__)


@app.route("/login")
def login():
    name, age = "", ""
    if name != 'zhansan' or age != '12':
        # 可以传入标准的HTTP状态码(否则不生效报错)
        abort(500)
    return 'login success'


# 对不同的HTTP状态码，可以自定义异常信息
@app.errorhandler(500)
def error_msg(error):
    # 自定义异常信息的函数必须接收一个参数，这个参数就是原本的错误信息
    return '404 file not found. \r\n%s' % error


if __name__ == "__main__":
    app.run(debug=True)