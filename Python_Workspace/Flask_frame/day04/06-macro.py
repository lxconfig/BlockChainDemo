from flask import Flask, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    '''使用宏的模板'''
    return render_template('macro.html')


if __name__ == "__main__":
    app.run(debug=True)