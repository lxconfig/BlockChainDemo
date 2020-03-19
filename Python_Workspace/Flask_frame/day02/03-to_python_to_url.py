from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter


app = Flask(__name__)


class MyConverter(BaseConverter):
    # url_map参数必须写, regex是固定写法，不能改
    def __init__(self, url_map, regex):
        self.regex = regex
        # 调用父类的__init__()方法
        super(MyConverter, self).__init__(url_map)
    
    def to_python(self, value):
        # value = 通过正则匹配出来的结果
        # to_python()的作用在于，可以对匹配出来的结果做一些处理
        print("to_python called")
        # 一般直接返回给视图函数
        # 执行顺序： 正则匹配 --> 结果先给value --> 处理完后在返回给mobile
        return value
    
    def to_url(self, value):
        # 在url_for()调用时，跳转到这个函数来执行
        # value = 正则匹配的结果
        # 执行顺序: 
        # mobile的值经过正则匹配 --> 结果给value --> 处理完 --> 返回完整的url做为url_for的返回值 --> 跳转
        print("to_url called")
        return value


app.url_map.converters['re'] = MyConverter


@app.route('/index/<re(r"1[345789]\d{9}"):mobile>')
def index(mobile):
    return 'mobile = %s' % mobile


@app.route("/login")
def login():
    # url反向解析时，要跳转的视图函数如果需要参数，则用不定长参数的形式写
    url = url_for("index", mobile='18370850448')
    return redirect(url)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)