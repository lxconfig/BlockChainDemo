# coding:utf-8
# time: 2019/8/27 14:29
# File: 04-自定义异常.py

class CustomError(Exception):  # 异常都继承自Exception类
    def __init__(self, code=100, message="自定义异常"):
        self.code = code
        self.message = message


try:
    print("aaaa")
    raise CustomError(404, "异常")  # raise引发一个异常
except CustomError as c:  # 出现异常后执行的操作
    print("异常代码:%s,异常信息:%s" % (c.code, c.message))
# else:  # 没有异常执行的操作
#     print("无异常")
finally:  # 有无出现异常都会执行
    print("finished")