# -*- coding:utf-8 -*-
# time: 2019/05/06 15:02
# File: 共享全局变量.py
import threading
import time

numbers = 100
num = [11, 22]

def test1(num):
    global numbers
    numbers += 100
    num.append(33)
    print("-----in test1() numbers=%d" % numbers)
    print("-----in test1() num=%s" % str(num))

def test2(num):
    print("-----in test2() numbers=%d" % numbers)
    print("-----in test2() numbers=%s" % str(num))

def main():
    t1 = threading.Thread(target=test1, args=(num,))
    t2 = threading.Thread(target=test2, args=(num,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("-----in main() numbers=%d" % numbers)
    print("-----in main() numbers=%s" % str(num))


if __name__ == '__main__':
    main()