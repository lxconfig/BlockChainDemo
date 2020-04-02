from . import api
# import logging  # 可以通过logging模块记录日志信息
from flask import current_app   # 也可以用current_app记录，它包含了logging模块的那个全局日志对象
from ihome import db, models


@api.route("/index")
def index():
    current_app.logger.error("error msg")
    current_app.logger.warning("warning msg")
    current_app.logger.info("info msg")
    current_app.logger.debug("debug msg")
    return "index page"