from flask import Flask, request


app = Flask(__name__)


@app.route("/index", methods=["POST", "GET"])
def index():
    # request中包含了前端发来的所有数据
    # request.form可以查询表单格式的数据
    # get同名只取第一个, getlist取全部
    name = request.form.get('name')
    age = request.form.get('age')
    name_list = request.form.getlist('name')

    # request.data可以查询请求体中的数据，比如JSON格式的数据
    data = request.data
    print(data)

    # request.headers可以提取请求头
    header = request.headers
    print(header)

    # request.method可以提取访问方式
    method = request.method
    print(method)

    # request.args可以提取查询字符串QueryString的数据，即url中带着的参数  /index?city=gz&country=china
    city = request.args.get("city")
    country = request.args.get("country")

    return 'hello name=%s, age=%s, city=%s, country=%s, name_list=%s' % (name, age, city, country, name_list)


if __name__ == "__main__":
    app.run(debug=True)