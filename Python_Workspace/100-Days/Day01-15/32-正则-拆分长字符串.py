# -*- coding:utf-8 -*-
# time: 2019/8/12 10:40
# File: 32-正则-拆分长字符串.py

import re

def main():
    """
    拆分长字符串
    """
    file = "窗前明月光，疑是地上霜。举头望明月，低头思故乡。"
    ret = re.compile(r'[，。,.]')
    file1 = re.split(ret, file)
    file1.remove("") # 匹配完最后有一个空字符串""
    print(file1)


if __name__ == '__main__':
    main()