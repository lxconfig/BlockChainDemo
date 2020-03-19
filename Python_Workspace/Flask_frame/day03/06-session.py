from flask import Flask, session

app = Flask(__name__)

"""
    Django中session的数据是保存在数据库中的，而flask是保存在cookie中
    浏览器请求某视图函数时，若该视图函数设置了session，则服务器在返回时，会设置一个cookie，即 session_id
    以后浏览器在访问到session中的数据时，就可以通过session_id来找到

    如果不在cookie中保存session_id，也是可以获取到session数据的，只要在url中通过参数的形式拼接上session_id
    比如: 先请求login页面，成功后，数据库保存了session数据，并返回session_id，服务器重定向到首页时，url为127.0.0.1/index?session_id=1
    但通过url的方式，没办法设置有效期
"""


# 设置session时，一定要用到参数SECRET_KEY
# 用来对session的数据进行加密
app.config['SECRET_KEY'] = 'sgsrrehrergnsjgsjmn'


@app.route("/login")
def login():
    '''设置session'''
    # 直接通过键值对的方式设置session
    session['name'] = 'zhangsan'
    session['age'] = 18
    return 'set session success'


@app.route("/index")
def index():
    '''获取session中的值'''
    name = session.get("name")
    return 'hello %s ' % name



if __name__ == "__main__":
    app.run(debug=True)