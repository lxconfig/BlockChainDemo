# -*- coding:utf-8 -*-
# time: 2019/05/06 11:10
# File: 查看正在运行的线程.py
import threading
import time

def sing():
    for i in range(5):
        print("singing....")
        time.sleep(1)

def dance():
    for i in range(10):
        print("dancing....")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数：%d" % length)
        if length <= 1:
            break
        time.sleep(0.5)

if __name__ == '__main__':
    main()