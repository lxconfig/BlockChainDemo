from flask import Flask, url_for, redirect


app = Flask(__name__)


# 定义路由，通过methods参数限定访问方式
@app.route("/hello", methods=['GET'])
def index():
    return 'hello flask'


# 多个路由对应一个视图函数
# 输入哪个路径都可以访问
@app.route("/view")
@app.route("/func")
def view_func():
    return 'hello'


# 同一个路由对应多个视图函数
# 此时只有第一个视图函数能被访问
# 除非两个视图函数的访问方式不同
@app.route('/hill')
def hill1():
    return 'hill1'


@app.route("/hill")
def hill2():
    return 'hill2'


# url反向解析
# Django中  reverse("namespace:name")
# Flask中使用 url_for("视图函数名")
@app.route("/login")
def login():
    return redirect(url_for('index'))


if __name__ == "__main__":
    # 查看当前所有的路由映射
    print(app.url_map)
    app.run(debug=True)