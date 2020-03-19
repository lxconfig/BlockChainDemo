# 第三种方式：
# 不手动添加字典的元素，而是用装饰器来添加
URL_FUNC_DICT = dict()

def route(url):  # 这里的url是文件的路径
    def set_func(func):  # func是函数的引用
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func()
        return call_func
    return set_func


# 路由添加正则表达式，减少字典中键值对的个数
# @route(r'add/\d+\.html')
# def add_focus():
#     return "add ok"

@route('index.py')
def index():
    return "这是index页面"


@route('login.py')
def login():
    return "这是login页面"


# 第二种方式：
# 添加一个字典类型的全局变量，用来保存请求的文件名与对应的函数
'''
URL_FUNC_DICT = {
    'index.py': index,
    'login.py': login,
}
'''


def application(environ, func_name):
    """
    支持WSGI协议的web框架
    environ: 是一个字典类型的参数，用于服务器给框架传递一些参数
    func_name: 是定义在服务器的一个函数引用，用于设置headers
    application()必须实现，主要用来返回body
    """
    # 设置响应头
    func_name("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ['file_path']

    '''更好判断执行函数的方法'''
    # 第一种方式：
    # if file_name == 'index.py':
    #     return index()
    # elif file_name == 'login.py':
    #     return login()
    # else:
    #     return "Hello World!"
    
    # 不用一堆if语句判断该执行哪个函数，而是用一个字典来取
    # 路由：根据file_name的不同，调用不同的函数
    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception:
        return "产生了异常%s" % file_name
