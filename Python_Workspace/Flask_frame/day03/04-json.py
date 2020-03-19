from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.route("/index")
def index():
    '''返回json格式的数据'''
    # # 1. 使用json模块构造json字符串
    # data = {"name": "zhangsan", "age": 23}
    # json_str = json.dumps(data)
    # print(json_str)
    # # 2. 修改响应头信息
    # return json_str, 200, {"Content-Type": "application/json"}

    # 或者使用jsonify(), 直接将上面两个步骤封装好了
    # 可以直接传入字典，或者用关键字参数
    return jsonify(city="gz", country="china")
    # return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)