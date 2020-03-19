import re


# 用装饰器来添加字典中的键值
URL_DICT = dict()

def set_dict(request_file):
    def set_func(func):
        URL_DICT[request_file] = func
        def call_func(*args, **kwargs):
            func(*args, **kwargs)
        return call_func
    return set_func


@set_dict('index.py')
def index(file_name, static_path):
    '''返回首页'''
    table = [['张三', 0], ['李四', 1], ['王五', 2]]
    tr_temp = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
    '''
    html = ''
    for line in table:
        html += tr_temp % (line[0], line[1])
    with open(static_path+'index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'{%content%}', html, content)
    # print(URL_DICT)
    return content

# 2. 用一个全局变量来保存 文件名 ---> 对应处理函数 的映射
# 问题在于：这个变量的键值需要人为添加补充
# 优化：考虑使用装饰器来自动添加
# URL_DICT = {
#     'index.py': index
# }


def application(environ, func_name):
    '''
        框架文件，用来处理请求的动态文件，遵循WSGI协议
    '''
    func_name("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ['file_name']
    static_path = environ['static_path']
    # 1. 通过if判断来确定要执行的处理函数
    # 问题在于：文件很多，要写很多if
    # 优化：用一个字典型的全局变量来保存
    # if file_name == 'index.py':
    #     # 返回响应体(响应内容)
    #     return index(file_name, static_path)

    try:
        func = URL_DICT[file_name]
    except Exception:
        return "产生异常%s" % file_name
    else:
        return func(file_name, static_path)


