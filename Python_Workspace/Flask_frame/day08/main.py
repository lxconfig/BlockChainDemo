from flask import  Flask
from define_blueprint import orders   # 导入定义好的蓝图
# from cart.views import app_cart
from cart import app_cart


app = Flask(__name__)


# 注册蓝图
app.register_blueprint(orders)
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route("/")
def index():
    return "index page gunicorn"


if __name__ == "__main__":
    print(app.url_map)
    app.run()