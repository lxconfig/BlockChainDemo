from flask import Flask, make_response, request


app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    '''设置cookie'''
    response = make_response("set success!")
    # 前者为键，后者为值，max_age表示过期时间，默认是浏览器关闭就过期
    # 要设置多个就再写一次
    response.set_cookie("flask", "python", max_age=3600)
    response.set_cookie("flask2", "python2")
    # 或者通过响应头的方式设置cookie
    response.headers['Set-Cookie'] = "Django=python; Expires=Thu, 12-Mar-2020 08:17:48 GMT; Max-Age=3600; Path=/"
    return response

@app.route("/get_cookie")
def get_cookie():
    value = request.cookies.get('Django')
    return value


@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("delete success!")
    # 根据键，删除cookie
    # 并不是真的删除flask键值对，而是将过期时间改为创建时间
    response.delete_cookie("flask")
    return response


if __name__ == "__main__":
    app.run(debug=True)