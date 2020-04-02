from flask import Blueprint


# 定义蓝图对象
api = Blueprint("api", __name__)


# 导入蓝图对象修饰的视图函数
from . import demo