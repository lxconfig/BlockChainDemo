from cart import app_cart
# from . import app_cart  # . 就代表当前路径
from flask import render_template


# 定义视图函数
@app_cart.route("/get_cart")
def get_cart():
    # 加载模板文件的时候，会先去总目录中寻找，再到自己这个小模块中寻找
    return render_template("cart.html")