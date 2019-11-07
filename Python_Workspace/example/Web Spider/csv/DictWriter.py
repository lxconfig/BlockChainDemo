# -*- coding:utf-8 -*-
# time: 2019/04/30 18:58
# File: DictWriter.py
import csv
import os

'''DictWriter类，可以写入字典形式的数据'''

# headers = ["name", "age"]
# data = [
#     {"name": "bob", "age": 23},
#     {"name": "joe", "age": 21},
#     {"name": "alex", "age": 12},
#     {"name": "rsy", "age": 132},
# ]
#
# with open("test1.csv", 'a+', newline="") as f:
#     csv_DictWriter = csv.DictWriter(f, headers)
#     csv_DictWriter.writeheader()  # 可以用来写入表头，但是存在问题，再次写入数据的话，表头又被写入
#     for row in data:
#         csv_DictWriter.writerow(row)

# 判断表头是否存在

headers = ["name", "age"]
data = [
    {"name": "bob", "age": 23},
    {"name": "joe", "age": 21},
    {"name": "alex", "age": 12},
    {"name": "rasaaaaaaa", "age": 132},
]
file_name = "test1.csv"
with open(file_name, 'w', newline="") as fps:
    csv_DictWriter = csv.DictWriter(fps, headers)
    csv_DictWriter.writeheader()

with open(file_name, "r") as f:
    csv_reader = csv.reader(f)
    list1 = [row for row in csv_reader]
    with open(file_name, "a+", newline="") as fp:
        csv_DictWriters = csv.DictWriter(fp, headers)
        if  list1[0] == headers:
            for rows in data:
                csv_DictWriters.writerow(rows)