# -*- coding:utf-8 -*-
# time: 2019/05/05 20:41
# File: demo1.py
import threading
import time

def sing():
    for i in range(5):
        print("sing.....")
        time.sleep(1)

def dance():
    for i in range(5):
        print("dancing...")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()