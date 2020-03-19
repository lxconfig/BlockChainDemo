from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)


# CSRF需要SECRET_KEY字段
app.config['SECRET_KEY'] = 'wetwewgrgw54we'


# 使用flask_wtf扩展可以帮助在后端进行数据的验证以及CSRF的验证
# 并且通过模型类的对象，可以快速编写前端的表单代码
# 定义表单模型类(类似Django中的模型类)
class RegisterForm(FlaskForm):
    '''注册表单模型类'''
    # 定义出注册表单需要的字段
    # StringField表示字段的类型，label表示描述信息，validators表示该字段需要满足的条件，DataRequired表示该字段不能为空，message表示出错的提示信息
    username = StringField(label='用户名', validators=[DataRequired(message="用户名不能为空")])
    password = PasswordField(label='密码', validators=[DataRequired(message='密码不能为空')])
    password2 = PasswordField(label='确认密码', validators=[DataRequired(message='确认密码不能为空'), EqualTo("password", message='密码输入不一致')])
    submit = SubmitField(label='提交')


@app.route("/register", methods=['POST', "GET"])
def register():
    # 先创建模型类的对象
    # 不论是get/post请求，都需要创建form对象
    # post请求时，前端传递的数据都保存为form的属性
    form = RegisterForm()
    # 验证数据
    # validata_on_submit()只有在数据都通过验证时才为真,包括csrf验证
    if form.validate_on_submit():
        user_name = form.username.data
        pwd = form.password.data
        pwd2 = form.password2.data
        session['username'] = user_name
        print(user_name, pwd, pwd2)
        return redirect(url_for('index'))

    # 再传递给模板
    return render_template('register.html', form=form)


@app.route("/index")
def index():
    username = session.get('username', '')
    return 'hello %s ' % username

if __name__ == "__main__":
    app.run(debug=True)