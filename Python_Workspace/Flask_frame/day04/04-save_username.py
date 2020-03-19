from flask import Flask, redirect, render_template, request, url_for, session


app = Flask(__name__)


app.config['SECRET_KEY'] = 'sgrgrrhrehrh'

@app.route("/login", methods=['GET', "POST"])
def login_check():
    if request.method == "POST":
        # 获取前端的数据
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember")

        if username == 'zhangsan' and password == '123':
            session['isLogin'] = True
            response = redirect(url_for('index'))
            if remember:
                response.set_cookie('username', username)
        else:
            return redirect(url_for('login'))
        return response
    else:
        if 'isLogin' in session:
            return redirect('index')
        else:
            if 'username' in request.cookies:
                username = request.cookies.get('username')
            else:
                username = ''
            return render_template('login.html', username=username)


'''
@app.route("/login")
def login():
    if 'username' in request.cookies:
        username = request.cookies.get('username')
    else:
        username = ''
    return render_template('login.html', username=username)
'''


@app.route("/index")
def index():
    username = request.cookies.get('username')
    return render_template('index2.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)