from flask import Flask, current_app
# current_app就相当于app对象


app = Flask(__name__)


# 配置参数的使用方式
# 1. 通过文件配置 from_pyfile读取配置文件
# app.config.from_pyfile('config.cfg')

# 2. 通过类配置
class Config:
    DEBUG = True
# app.config.from_object(Config)

# 3. 直接往app.config(是一个类似字典的对象)中添加键值对
# app.config['DEBUG'] = True

# 4. 通过一个字典设置
Config_dict = {
    "DEBUG": True
}
app.config.from_mapping(Config_dict)


@app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    # 启动时的一些配置参数
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )