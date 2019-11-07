# coding:utf-8
# time: 2019/8/21 16:28
# File: 821test.py

import datetime
import os
def main():
    a = [1,2,3,4]
    b = {"a": 1, "b": 2}
    c = {1, 2, 3} # 集合
    print(id(a))
    print(id(b))
    print(id(c))

    a[0], a[1] = 0, 7
    b["a"] = 3
    c.add(4)


    print(id(a))
    print(id(b))
    print(id(c))

    time = datetime.datetime.now()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))

    os.remove("log.log")

if __name__ == '__main__':
    main()