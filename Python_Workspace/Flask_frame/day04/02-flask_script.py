from flask import Flask
from flask_script import Manager


app = Flask(__name__)

# 创建管理类对象，用来管理相应的flask应用对象
manager = Manager(app)


@app.route("/index")
def index():
    return 'index page'


if __name__ == "__main__":
    # 用管理类对象来启动flask应用
    # 此时启动flask要用命令行的形式启动
    # python xxxx.py runserver/shell
    manager.run()    