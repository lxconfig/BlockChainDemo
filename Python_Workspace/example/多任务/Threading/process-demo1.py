# -*- coding:utf-8 -*-
# time: 2019/05/08 19:57
# File: process-demo1.py
import multiprocessing
import time

def test1():
    while True:
        print("----1-----")

def test2():
    while True:
        print("-----2----")

def main():
    # 创建进程
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    # 启动进程
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()