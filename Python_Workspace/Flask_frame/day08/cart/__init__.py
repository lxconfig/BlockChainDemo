'''
@Author: lixuan
@Date: 2020-03-27 15:28:18
@LastEditTime: 2020-03-27 15:37:24
@Description: 以目录的形式定义蓝图
'''
from flask import Blueprint


# 每次cart被导入时，都会先执行__init__.py文件，所以可以在__init__.py文件中创建出蓝图对象
# 让小模块使用自己目录下的templates和static文件夹，要显式的指明出来
app_cart = Blueprint('app_cart', __name__, template_folder="templates", static_folder="static")


# 当__init__.py文件文件被执行时，加载视图
from .views import get_cart