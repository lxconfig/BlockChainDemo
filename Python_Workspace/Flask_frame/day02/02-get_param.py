from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)


# 获取参数
# Flask中通过 转换器 来获取参数
# 转换器有 int/float/path/字符串 四种类型，默认是字符串
# path会提取路径，如 127.0.0.1:5000/index/c/d/c/index 提取为 c/d/c/index
# @app.route("/index/<goods_id>")
@app.route("/index/<int:goods_id>")
def goods_detail(goods_id):
    return 'goods detail %s' % goods_id


# 除了Flask定义好的转换器外，可以自定义转换器
# 1. 创建转换器类，继承自BaseConverter
class MyConverter(BaseConverter):
    # url_map参数必须写, regex是固定写法，不能改
    def __init__(self, url_map, regex):
        self.regex = regex
        # 调用父类的__init__()方法
        super(MyConverter, self).__init__(url_map)

# 2. 将自定义的转换器，添加到flask的应用中
# 是一个字典类型的值，可以添加
app.url_map.converters['re'] = MyConverter

# 3. 写路由规则
# 路由中写的正则表达式，会被传入到MyConverter类中保存
@app.route('/login/<re(r"1[345789]\d{9}"):mobile>')
def login(mobile):
    return 'mobile = %s' % mobile


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)