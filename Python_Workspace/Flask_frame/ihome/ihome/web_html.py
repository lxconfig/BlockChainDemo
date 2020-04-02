
"""
    此文件的目的是为了给前端提供静态文件
"""


from flask import Blueprint, current_app, make_response
from flask_wtf import csrf


# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)


# 访问方式: 127.0.0.1:5000/
# 127.0.0.1:5000/index.html


@html.route("/<re(r'.*'):file_name>")
def get_html(file_name):
    """提供html文件"""
    if not file_name:
        file_name = "index.html"

    # favicon.ico是网页标签右上角的一个小图标，浏览器会自己请求这个资源
    if file_name != "favicon.ico":
        file_name = "html/" + file_name
    
    # 生成一个csrf_token值
    csrf_token = csrf.generate_csrf()

    # flask提供的返回静态文件的方法，默认会去静态文件夹static中查找
    response = make_response(current_app.send_static_file(file_name))

    # 设置cookie的值
    response.set_cookie("csrf_token", csrf_token)

    return response