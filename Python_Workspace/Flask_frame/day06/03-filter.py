from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func


app = Flask(__name__)
pymysql.install_as_MySQLdb()

class Config():
    # 数据库的地址、账号、密码等信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:lixuan@127.0.0.1:3306/flaskTest"

    # 设置自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 设置每次请求结束后自动提交数据库的改动  不推荐使用!
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 查询时显示原始的sql语句
    # SQLALCHEMY_ECHO = True

app.config.from_object(Config)
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

    def __repr__(self):
        '''让对象显示的时候更直观'''
        return "Role object: name=%s" % self.name


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

    def __repr__(self):
        '''让对象显示的时候更直观'''
        return "User object: name=%s" % self.name


if __name__ == "__main__":
    # 过滤查询
    # 表示 且 的关系
    # 数据不存在不会报错
    user = User.query.filter_by(name='zhangsan', role_id=1).first()
    print(user.name)

    # filter中的条件必须指明来源，且要用 == 
    data = User.query.filter(User.name=='wangwu', User.role_id==2).all()
    print(data[0].email)

    # or_ 表示 或 的关系
    file = User.query.filter(or_(User.name=="lisi", User.role_id==2)).all()
    print(file)

    # offset(2) 跳过2条数据，从第3条开始取
    off = User.query.offset(2).all()
    print(off[0].name, off[1].name)

    # limit(2) 限制取数据个数，只取2条
    lim = User.query.offset(1).limit(2).all()
    print(lim[0].name, lim[1].name)

    # order_by()  排序
    ords = User.query.order_by(User.id.desc()).all()
    print(ords[0].name)

    # group_by()  分组
    # User.role_id, func.count(User.role_id) 表示分组之后的字段名
    group = db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()
    print(group)

    # 关联查询
    # 一查多
    ro = Role.query.get(1)
    print(ro.users[0].name, ro.users[1].name)  # ro.users中保存的就是User类的对象，也就是对应于role_id=1的用户

    # 多查一
    user_object = User.query.get(1)
    # 没有定义backref的话，用 Role.query.get(user_object.role_id)
    print(user_object.role.name)

    # print(User.query.get(1))