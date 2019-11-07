# -*- coding:utf-8 -*-
# time: 2019/04/30 18:46
# File: csv_reader.py

import csv

# csv文件读取
# with open("test.csv", 'r') as f:
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         print(csv_reader.line_num, row)  # csv_reader.line_num输出行号


# 跳一行读取
with open("test1.csv", 'r') as f:
    csv_reader = csv.reader(f)
    # for i in range(0, 2):
    #     head_row = next(csv_reader)  # 跳过首行数据,配合循环可以跳过多行
    list1 = [row for row in csv_reader]
    print(list1[0])