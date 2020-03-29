from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pymysql
import json


app = Flask(__name__)
pymysql.install_as_MySQLdb()


class Config():
    # 创建一些配置项
    SQLALCHEMY_DATABASE_URI = "mysql://root:lixuan@127.0.0.1:3306/author_book"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "sgsngoe35sodig9"


app.config.from_object(Config)
db = SQLAlchemy(app)


# 1. 创建模型类  Author  Book
class Author(db.Model):
    """作者模型类"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True)
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


# 5. 定义表单模型类
class AuthorBookForm(FlaskForm):
    """作者书籍表单模型类"""
    author_name = StringField(label="作者", validators=[DataRequired(message="请填入作者")])
    book_name = StringField(label="书籍", validators=[DataRequired(message="请填入书籍")])
    submit = SubmitField(label="提交")


# 3. 定义视图函数
@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    # 验证数据完整性
    if form.validate_on_submit():
        # 验证通过, 拿到数据，添加到数据库
        author_name = form.author_name.data
        book_name = form.book_name.data

        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()

    # 查询数据库，显示作者和书籍信息
    authors = Author.query.all()
    # books = Book.query.all()
    # return render_template('index.html', books=books)
    return render_template('index.html', authors=authors, form=form)

# 4. 定义模板


# 6. 补充模板

# 7. 定义删除书籍的视图函数  用get或者post方式删除
'''
# post方式 假定前后端传递的json格式的数据
@app.route("/delete_book", methods=['POST'])
def delete_book():
    # 获取前端发来的json数据
    # req_data = request.data
    # data = json.loads(req_data)
    # book_id = data["book_id"]
    # 使用get_json()将前端发送的json数据解析成字典
    # 要求Content-Type: application/json
    req_data = request.get_json()
    book_id = req_data["book_id"]

    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    resp_data = {"code":0}

    return jsonify(resp_data)
'''
# get方式  /delete_book/xx
# /delete_book?book_id=xx   用request.args.get()
@app.route("/delete_book/<int:book_id>", methods=['GET'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    # 2. 添加数据到数据库
    '''
    db.drop_all()
    db.create_all()
    author1 = Author(name='唐家三少')
    author2 = Author(name='爱吃西红柿')
    author3 = Author(name='天蚕土豆')
    author4 = Author(name='肖潜')
    db.session.add_all([author1, author2, author3, author4])
    db.session.commit()

    book1 = Book(name='斗罗大陆', author_id=author1.id)
    book2 = Book(name='吞噬星空', author_id=author2.id)
    book3 = Book(name='斗破苍穹', author_id=author3.id)
    book4 = Book(name='妖魔转', author_id=author4.id)
    db.session.add_all([book1, book2, book3, book4])
    db.session.commit()
    '''
    app.run(debug=True, host='0.0.0.0')