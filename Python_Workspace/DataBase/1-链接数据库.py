# -*- coding:utf-8 -*-
# time: 2019/06/26 13:05
# File: 1-Connection对象.py
import pymssql

def conn():
    connect = pymssql.connect("(local)", "lx", "shisan", "TestDB")
    if connect:
        print("连接成功")
    return connect

if __name__ == '__main__':
    conn = conn()
