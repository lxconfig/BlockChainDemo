'''
@Author: lixuan
@Date: 2020-03-27 14:54:18
@LastEditTime: 2020-03-27 15:00:06
@Description: 蓝图用于划分功能模块
'''
from flask import Blueprint


# 1. 创建蓝图对象
# orders 代表蓝图的名称
orders = Blueprint('orders', __name__, url_prefix='/orders')


# 2. 用蓝图对象创建视图函数
@orders.route("/get_orders")
def get_orders():
    return 'get orders page'


# 3. 在主模块中注册蓝图