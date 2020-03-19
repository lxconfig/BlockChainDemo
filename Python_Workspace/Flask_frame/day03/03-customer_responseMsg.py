from flask import Flask, make_response


app = Flask(__name__)


@app.route("/index")
def index():
    '''自定义响应信息'''
    
    # 1. 用元组的方式,分别返回 响应体, 状态码, 响应头(可省略)
    # return 'index page', 200, [('flask', 'python'), ('city', 'gz')]
    # 响应头还可以用字典的方式返回
    # return 'index page', 200, {'flask': 'python', 'city': 'gz'}
    # 状态码不要求是HTTP标准状态码，可以随便写
    # return 'index page', '666 flask', [('flask', 'python'), ('city', 'gz')]

    # 2. 通过make_response()设置
    response = make_response("index page2")  # 设置响应体
    response.status = '999 flask'            # 设置状态码
    response.headers['country'] = 'china'    # 设置响应头
    return response

if __name__ == "__main__":
    app.run(debug=True)