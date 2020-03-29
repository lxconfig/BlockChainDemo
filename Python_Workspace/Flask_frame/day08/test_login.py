'''
@Author: lixuan
@Date: 2020-03-28 14:47:15
@LastEditTime: 2020-03-28 14:48:36
@Description: 单元测试之测试视图函数
'''
import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
    """构造单元测试案例"""

    def setUp(self):
        """在测试之前，先执行"""
        self.client = app.test_client()
        # 开启flask的测试模式
        # 作用: 在视图函数抛出异常时，单元测试文件能正常获取到这个异常
        # app.config["TESTING"] = True
        app.testing = True

    # 测试函数必须是test_ 开头
    def test_empty_username_password(self):
        """测试用户名或密码为空的情况"""

        # # 使用flask提供的web请求客户端
        # client = app.test_client()
        
        # 利用客户端模拟发送请求
        # post/get
        ret = self.client.post("/login", data={})

        # 获取请求响应体数据
        response = ret.data
        response = json.loads(response)

        # 进行断言测试
        self.assertIn("code", response)
        self.assertEqual(response["code"], 0)

    def test_wrong_username_password(self):
        data = {
            "user_name": "zhangsan",
            "password": "saf"
        }
        ret = self.client.post("/login", data=data)

        response = json.loads(ret.data)

        self.assertIn("code", response)
        self.assertEqual(response["code"], 2)
    
    def test_right_username_password(self):
        data = {
            "user_name": "zhangsan",
            "password": "123"
        }
        ret = self.client.post("/login", data=data)

        response = json.loads(ret.data)

        self.assertIn("message", response)
        self.assertEqual(response["code"], 1)


if __name__ == "__main__":
    # 通过main()执行全部测试案例
    unittest.main()