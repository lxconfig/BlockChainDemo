from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    # 渲染模板时，直接传入模板名和参数，参数可以不用字典传递
    # 用字典传递也可以，写成 **data
    data = {
        'name': 'zhangsan',
        'gender': 'male',
        'dict': {'city': 'gz'},
        'list': [1,2,3,4,5],
        'age': 19
    }
    return render_template('index.html', **data)


# 自定义过滤器
# 1. 定义函数+注册过滤器
def filter_list(li):
    return li[::2]
# 注册过滤器，li2表示在模板文件中使用这个过滤器的名字
app.add_template_filter(filter_list, 'li2')


# 2. 定义函数+装饰器
# 也是传入在模板文件中使用的名字
@app.template_filter('li3')
def filter_list2(li):
    return li[::3]


if __name__ == "__main__":
    app.run(debug=True)    