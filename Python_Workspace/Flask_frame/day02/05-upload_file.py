from flask import Flask, request


app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    # request.files可以接收前端上传的文件
    # file_obj是一个文件对象
    file_obj = request.files.get("pic")
    if not file_obj:
        return "未上传文件"
    
    # 保存文件
    # with open("./test.png", 'wb') as f:
    #     f.write(file_obj.read())
    # 可以直接调用save()方法
    file_obj.save('./test.png')
    return '上传成功'

if __name__ == "__main__":
    app.run(debug=True)