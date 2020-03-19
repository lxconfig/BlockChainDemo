from flask import Flask


'''
    :param import_name: 导包路径，也就是项目目录的位置，一般传入__name__,表示当前目录
    :param static_url_path: 静态资源的访问路径，即在浏览器访问静态资源的前缀，如: 127.0.0.1:5000/python/index.html 默认是static
    :param static_folder: 静态资源的目录，默认是static
    :param template_folder: 模板文件的目录，默认是templates
'''
app = Flask(
    import_name=__name__,
    static_url_path='/python',
    static_folder='static',
    template_folder='templates',
)


@app.route("/")
def index():
    return 'hello flask2'

if __name__ == "__main__":
    app.run()