# -*- coding:utf-8 -*-
# time: 2019/04/29 20:01
# File: csv_rw.py
import csv


# csv文件写入
data = [("zimu", "shuzi", "qqq"), (1,2,3), (4,5,6)]
with open("test.csv", 'a+', newline="") as f:
    csv_writer = csv.writer(f)
    # csv_writer.writerow(data)  # 单行写入
    csv_writer.writerows(data)  # 多行写入

