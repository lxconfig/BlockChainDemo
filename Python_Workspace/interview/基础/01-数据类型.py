# coding:utf-8
# time: 2019/8/27 14:15
# File: 01-数据类型.py

def main():
    """列表、字典、集合是可变数据类型(修改值，地址不变)
    元组、整型、字符串、bool是不可变数据类型"""
    a = [1,2,3,4]
    b = {"a":1, "b":2}
    c = {1,2,3,4} # 集合
    print(id(a))
    print(id(b))
    print(id(c))

    a[0], a[1] = 9, 10
    b["c"] = 3
    c.add(4)
    print(id(a))
    print(id(b))
    print(id(c))




if __name__ == '__main__':
    main()