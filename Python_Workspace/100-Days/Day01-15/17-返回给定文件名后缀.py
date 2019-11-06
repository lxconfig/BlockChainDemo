# -*- coding:utf-8 -*-
# time: 2019/8/6 14:24
# File: 17-返回给定文件名后缀.py


def main(filename):
    """
    返回给定文件的后缀名
    :param filename: 文件名
    :return: 后缀名
    """
    try:
        prefix, suffix = filename.split(".")
    except ValueError:    # 发生异常后做什么
        return "无后缀"
    else:
        return "." + suffix


if __name__ == '__main__':
    filename = str(input("输入文件名："))
    print(main(filename))