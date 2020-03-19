from flask import Flask, make_response, request, url_for, redirect


app = Flask(__name__)


@app.route("/login", methods=['POST'])
def login():
    '''登录视图'''
    name = request.form.get('name')
    pwd = request.form.get("password")

    if name == 'zhangsan' and pwd == '123':
        # 登录成功跳转到首页
        response = redirect(url_for("index"))
        response.set_cookie('name', name, max_age=1)
        return response
    else:
        return "error"


@app.route("/index")
def index():
    '''首页视图'''
    name = request.cookies.get("name")
    print(name)
    return 'welcome index page %s' % name


if __name__ == "__main__":
    app.run(debug=True)