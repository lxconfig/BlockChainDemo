# -*- coding:utf-8 -*-
# time: 2019/06/26 15:04
# File: 3-增删改查.py

import pymssql
import connect_db  # 不执行conn = conn()

# conn = pymssql.connect("(local)", "lx", "shisan", "TestDB")
conn = connect_db.conn()

if conn:
    cur = conn.cursor()
    cur.execute("insert into TestDB2 values (3)")
    cur.execute("select * from TestDB2")
    row = cur.fetchone()  # 读取查询结果
    print(row)
    conn.commit()
    cur.close()
    conn.close()
    print("插入成功")