'''
@Author: lixuan
@Date: 2020-03-28 15:06:29
@LastEditTime: 2020-03-28 17:37:12
@Description: 单元测试之测试数据库操作
'''
import unittest
from author_book import Author, app, db


class DatabaseTest(unittest.TestCase):
    """数据库单元测试案例"""

    def setUp(self):
        app.testing = True
        # 测试中不能使用真实环境的数据库
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:lixuan@127.0.0.1:3306/flask_test"
        db.create_all()

    def test_add_author(self):
        """测试数据添加作者的操作"""
        author = Author(name="zhangsan")
        db.session.add(author)
        db.session.commit()
        
        result = Author.query.filter_by(name="zhangsan").first()

        self.assertIsNotNone(result)
    
    def tearDown(self):
        """在所有测试结束后执行，一般用来做清理操作"""
        db.session.remove()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()