# -*- coding:utf-8 -*-
# time: 2019/8/6 14:04
# File: 15-跑马灯文字.py

import os
import time

def main():
    content = "广东工业大学欢迎您"
    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()