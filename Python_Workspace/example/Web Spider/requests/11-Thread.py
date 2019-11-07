# -*- coding:utf-8 -*-
# time: 2019/03/16 15:22
# File: 11-Thread.py

import time
import threading


'''
# 一个主线程，主线程在运行
def sing():
    for i in range(1, 6):
        print("I am singing")
        time.sleep(1)
def dance():
    for i in range(1, 6):
        print("I am dancing")
        time.sleep(1)
def main():
    sing()
    dance()
'''

# 面向过程的方式使用线程
# 一个主线程，两个子线程（sing线程，dance线程）
'''
def sing(a):
    print("线程为%s,接收的参数%s" % (threading.current_thread().name, a)) # 当前线程名字
    for i in range(1, 6):
        print("I am singing")
        time.sleep(1)
def dance(a):
    print("线程为%s,接收的参数%s" % (threading.current_thread().name, a)) # 当前线程名字
    for i in range(1, 6):
        print("I am dancing")
        time.sleep(1)

def main():
    a = "qwer"
    # 创建sing子线程
    tsing = threading.Thread(target=sing, name="唱歌", args=(a,))
    # 创建dance子线程
    tdance = threading.Thread(target=dance, name="跳舞", args=(a, ))
    # 启动线程
    tsing.start()
    tdance.start()
    # 让主线程等待子线程结束之后再结束
    tsing.join()
    tdance.join()
    # 这里是主线程在运行
    print("这是主线程")
'''

# 面向对象的方式使用线程
# 写一个类，继承自threading.Thread
class SingThread(threading.Thread):
    def __init__(self, name, a):
        # 调用父类的构造函数
        super().__init__()
        self.name = name
        self.a = a
    def run(self):
        print("线程为%s,接收的参数%s" % (self.name, self.a))
        for i in range(1, 6):
            print("I am singing")
            time.sleep(1)
class DanceThread(threading.Thread):
    def __init__(self, name, a):
        super().__init__()
        self.name = name
        self.a = a
    def run(self):
        print("线程为%s,接收的参数%s" % (self.name, self.a))
        for i in range(1, 6):
            print("I am dancing")
            time.sleep(1)
def main():
    # 创建线程(用自定义的继承至threading.Thread的类)
    tsing = SingThread("唱唱","123")
    tdance = DanceThread("跳跳","567")
    # 启动线程,自动执行run方法
    tdance.start()
    tsing.start()
    # 让主线程等待子线程结束
    tsing.join()
    tdance.join()
    print("主线程和子线程全部结束")
if __name__ == '__main__':
    main()
