from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map
from flask_session import Session
from flask_wtf import CSRFProtect
from logging.handlers import RotatingFileHandler
from ihome.utilis.commons import MyConverter

import logging
import redis
import pymysql


# 创建数据库工具对象，此时没有绑定app对象
db = SQLAlchemy()
pymysql.install_as_MySQLdb()


# 创建redis链接对象，用做缓存
# 不再函数外面创建是因为开发和生产环境的redis数据库可能不一样
redis_store = None


# 记录日志文件
# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)

# 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存的日志文件的个数上限(超过上限会删除)
# 旧的日志文件改为log1
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)

# 创建日志记录的格式
formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")

# 给日志记录器设置格式
file_log_handler.setFormatter(formatter)

# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)


# 工厂模式
# 像工厂一样，根据给的需求，定制app对象
def create_app(config_name):
    '''
    @description: 创建flask的应用对象
    @params: config_name: str 配置模式的名字  ("develop", "product")
    @return: 
    '''
    
    app = Flask(__name__)
    config_class = config_map[config_name]
    app.config.from_object(config_class)

    # 此时绑定上app对象，这是所有flask扩展都拥有的方法
    db.init_app(app)

    # 初始化redis工具对象
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # 利用flask-session,将session数据保存到redis中，而不是cookie中
    Session(app)

    # 补充csrf防护
    CSRFProtect(app)

    # 为flask添加自定义的转换器
    app.url_map.converters["re"] = MyConverter

    # 注册蓝图，此时再导入蓝图对象api可以防止循环导包发生
    # 否则在视图函数中要使用db时，就会发生循环导包
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")

    # 注册提供静态文件的蓝图
    from ihome.web_html import html
    app.register_blueprint(html)

    return app