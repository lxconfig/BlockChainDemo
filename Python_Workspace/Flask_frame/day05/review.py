from flask import Flask, url_for, redirect, request, abort, make_response, jsonify, session, render_template
from werkzeug.routing import BaseConverter
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


# flask应用对象的一些配置
app = Flask(
    import_name=__name__,
    static_url_path='/index',  # url中静态资源的目录
    static_folder='static',   # 文件中静态资源的目录
    template_folder='templates'  # 模板文件的目录
)


@app.route("/index", methods=["POST", "GET"])
def index():
    return 'index page'


# 读取配置参数
# 1. 从文件中读取
app.config.from_pyfile('config.cfg')

# 2. 从类中读取
class MyConfig():
    DEBUG = True
app.config.from_object(MyConfig)

# 3. 直接向键值对中添加
app.config['DEBUG'] = True

# 4. 从字典中读取
myconfig = {
    "DEBUG": True
}
app.config.from_mapping(myconfig)


# 获取url中的部分数据作为参数
# 可以用转换器获取 int/float/path/默认字符串
@app.route("/login/<path:user_id>", methods=["POST", "GET"])
def login(user_id):
    return 'login page %s' % user_id

# 还可以自定义转换器
class MyConverter(BaseConverter):
    def __init__(self, url_map, regex):
        self.regex = regex
        super().__init__(url_map)
    
    def to_python(self, value):
        # 参数返回给其他视图函数时使用
        return value
    
    def to_url(self, value):
        # url_for()中使用
        return value

# 将自定义的转换器类型添加到app对象中
app.url_map.converters['re'] = MyConverter

@app.route('/conver/<re(r"1[356789]\d{9}"):user_id>')
def conver(user_id):
    return 'converter test %s' % user_id

@app.route('/con')
def con():
    return redirect(url_for("conver", user_id='18370850448'))


# request获取前端发来的所有数据
# request.method 获取请求方式
@app.route("/post", methods=["POST"])
def post():
    # form表单数据
    name = request.form.get("name")
    age = request.form.get("age")

    # args查询字符串数据
    city = request.args.get("city")

    # data请求体, headers请求头
    data = request.data
    headers = request.headers

    # files获取上传的文件
    file_obj = request.files('pic')
    file_obj.save('test2.png')
    return name,age,city,data,headers


# 提前终止视图函数的运行，返回错误信息给前端
@app.route("/abort")
def abo():
    abort(403)
# 可以自定义错误信息
@app.errorhandler(403)
def handler_error(error):
    return "error %s" % error


# 自定义响应体的数据
@app.route("/resp")
def resp():
    # return "response content", "405", [('city', 'gz')]
    # return 'response content', '666 hh', {"city": "gz"}
    # 或者通过make_response设置
    response = make_response("response content")
    response.status = '999 xx'
    response.headers['city'] = 'gz'
    return response


# 返回json格式的数据
@app.route("/json")
def return_json():
    # data = {"city": 'gz'}
    # json_data = json.dumps(data)
    # return json_data, 200, {"Content-Type": 'application/json'}
    return jsonify(city='gz')


# cookie
@app.route("/cook")
def set_cookies():
    response = make_response("set cookie")
    response.set_cookie('python', 'flask', max_age=3600)
    return response

@app.route("/get_cook")
def get_cookies():
    data = request.cookies.get("python")
    return data


# session
app.config['SECRET_KEY'] = 'srgsjghsdgsgu54jdshguie7t4'
@app.route("/sess")
def set_sessions():
    session['username'] = 'zhangsan'
    return "set session ok"

@app.route("/get_sess")
def get_sessions():
    username = session.get("username")
    return username


# 钩子
@app.before_first_request
def before_first():
    # 在第一次请求之前调用
    print('before first request')

@app.before_request
def before_req():
    # 在请求处理之前调用
    print("before request")

@app.after_request
def after_req(response):
    # 在请求处理之后，且没有异常时调用
    # 接收视图函数的返回值，并交给前端
    print("after request")
    return response

@app.teardown_request
def teardown_req(response):
    # 在请求处理之后，无论是否有异常都调用
    print("teardown request")
    return response


# 模板
@app.route("/muban")
def muban():
    # 直接用关键字传参数，或者用字典传参数
    return render_template("muban.html", data=[1,2,3,4,5,6,7,8,9])


# 过滤器
# 1. 函数+注册过滤器
def myFilter(li):
    return li[::2]
app.add_template_filter(myFilter, 'myFilter')

# 2. 函数+装饰器
@app.template_filter("myFilter2")
def myFilter2(li):
    return li[::3]


# flask_wtf扩展: 帮助我们验证前端发来的数据，而不用写大量if else语句
# 1. 先定义出表单的模型类
class FormDataMoudle(FlaskForm):
    name = StringField(label="用户名", validators=[DataRequired(message="请输入用户名")])
    password = PasswordField(label='密码', validators=[DataRequired(message="请输入密码")])
    password2 = PasswordField(label='确认密码', validators=[DataRequired(message="请输入确认密码"), EqualTo("password", message="两次密码输入不一致")])
    submit = SubmitField(label="提交")

# 2. 定义视图函数
@app.route("/form", methods=["POST"])
def form_data():
    # 3. 不论哪种访问方式都需要先创建一个表单模型类的实例
    form = FormDataMoudle()

    if form.validate_on_submit():
        # 全部验证通过就跳转到index页面
        name = request.form.get("name")
        pwd = request.form.get("password")
        pwd2 = request.form.get('password2')
        return redirect(url_for('index'))
    # 否则回到表单页面，并显示错误信息
    # form中保存了错误信息
    return render_template("form_data.html", form=form)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )