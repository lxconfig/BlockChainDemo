from flask import Flask


# 创建flask的应用对象
# 表示使用当前目录作为项目目录
# 直接启动时，__name__=__main__, 被作为包导入时, __name__=文件名
# 不传或瞎传无意义的字符串时，flask还是会以当前的目录为准
app = Flask(__name__)


# 配置路由
# 与Django不同，没有单独的urls.py文件来保存 路由与视图函数的关系
@app.route('/')
def index():
    '''定义视图函数'''
    # 响应内容可以直接返回
    # 不需要HttpResponse("hello")
    return 'hello flask'


if __name__ == "__main__":
    # 启动flask项目
    # 可以直接在终端中运行,而不用像Django一样 python manage.py runserver
    app.run()