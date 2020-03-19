from flask import Flask


app = Flask(__name__)


@app.route("/index")
def index():
    print("index called")
    return 'index page'


@app.before_first_request
def handler_before_first_request():
    '''在第一次请求前被调用(在视图函数调用前)'''
    print("before_first_request called")


@app.before_request
def handler_before_request():
    '''在每次请求前被调用'''
    print("before_request called")


@app.after_request
def handler_after_request(response):
    '''在请求处理完(视图函数执行完)后被调用，前提时视图函数没有发生异常'''
    # 需要接收视图函数的返回值，并返回给前端
    print("after_request called")
    return response


@app.teardown_request
def handler_teardown_request(response):
    '''在请求处理完后被调用，无论视图函数是否有异常都会被调用，前提是在生产模式下，而不是debug模式'''
    print("teardown_request called")
    return response
    

if __name__ == "__main__":
    app.run()