# coding:utf-8
# time: 2019/8/27 14:19
# File: 02-获取当前日期.py

import datetime


def main():
    time = datetime.datetime.now()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))



if __name__ == '__main__':
    main()