# -*- coding:utf-8 -*-
# time: 2019/06/26 14:50
# File: 2-创建表.py

import pymssql

conn = pymssql.connect("(local)", "lx", "shisan", "TestDB")
if conn:
    print("连接成功")

# 创建游标对象，用来执行sql语句
cur = conn.cursor()
cur.execute("create table TestDB2(id varchar(20))")  # 执行sql
conn.commit()  # 提交
cur.close()  # 关闭游标
conn.close() # 关闭链接


