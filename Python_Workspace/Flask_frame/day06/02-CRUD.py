from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


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
    '''
    # insert data to database flaskTest
    # 1. 创建对象
    role1 = Role(name='admin')
    # 2. session记录对象任务
    db.session.add(role1)
    # 3. 提交任务到数据库
    db.session.commit()

    role2 = Role(name='staff')
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='zhangsan', email='1234@163.com', password='123', role_id=role1.id)
    us2 = User(name='lisi', email='wraf@163.com', password='234', role_id=role2.id)
    us3 = User(name='wangwu', email='ffgg@163.com', password='234', role_id=role2.id)
    us4 = User(name='zhaoliu', email='gkg@163.com', password='242', role_id=role1.id)

    # 一次提交多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
    '''

    '''
    # find data from database
    # 1. 类名.query.all()
    # 返回所有数据(类型是Role类的对象)
    li = Role.query.all()
    r = li[0]
    print(r.name)

    # 2. 类名.query.first()
    # 返回第一条数据(类型是User类的对象)
    first = User.query.first()
    print(first.email)

    # 3. 类名.query.get(主键) 一定要是主键
    # 返回对应主键的数据(类型是User类的对象)
    get_data = User.query.get(2)
    print(get_data.name)

    # 4. db.session.query(类名).all()
    # 5. db.session.query(类名).get(2)
    # 6. db.session.query(类名).first()
    '''
    
    '''
    # update data in database
    user = User.query.get(1)
    user.name = 'zhangsan1'
    db.session.add(user)
    db.session.commit()

    # 或者
    User.query.filter_by(name='zhangsan1').update({"name": "zhangsan2"})
    db.session.commit()
    '''

    # role_temp = Role(name='temp')
    # db.session.add(role_temp)
    # db.session.commit()

    # delete data from database
    roles = Role.query.filter(Role.name=='temp').first()
    db.session.delete(roles)
    db.session.commit()