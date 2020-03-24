from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

pymysql.install_as_MySQLdb()


# 通过类，创建一些数据库用到的参数
class Config():
    # 数据库的地址、账号、密码等信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:lixuan@127.0.0.1:3306/flaskTest"

    # 设置自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 设置每次请求结束后自动提交数据库的改动  不推荐使用!
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 查询时显示原始的sql语句
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)

# 创建数据库工具对象
db = SQLAlchemy(app)

# 创建模型类
class Role(db.Model):
    """用户角色模型类"""
    # 自定义表名
    __tablename__ = 'tbl_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    # 定义专门用于查询的字段
    # "User"：用于查询一个角色对应的用户
    # backref='role'： 用于查询一个用户对应的角色，依赖于外键role_id
    users = db.relationship("User", backref="role")


class User(db.Model):
    """用户模型类"""
    # 自定义表名
    __tablename__ = "tbl_users"

    # 创建数据库表中的字段
    id = db.Column(db.Integer, primary_key=True)  # 创建主键，整型时会自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    # 定义外键
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))


if __name__ == "__main__":
    # 清除数据库中所有的数据  不要随便使用!
    db.drop_all()

    # 创建所有的表
    db.create_all()