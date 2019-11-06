# -*- coding:utf-8 -*-
# time: 2019/8/9 15:25
# File: 27-素数写入文件中.py
import time

def calc_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2-t1)
    return wrapper


def is_prime(num):
    if num == 1:
        return num
    factor = []
    for i in range(1, num+1):
        if num % i == 0:
            factor.append(i)
    if len(factor) == 2:
        return num


@calc_time
def main():
    file_names = ["a.txt", "b.txt", "c.txt"]
    file_list = []
    try:
        for filename in file_names:
            file_list.append(open(filename, "w", encoding="utf-8"))
        for num in range(1, 10000):
            if is_prime(num):
                if num <= 99:
                    file_list[0].write(str(num) + '\n')
                elif num <= 999:
                    file_list[1].write(str(num) + '\n')
                else:
                    file_list[2].write(str(num) + '\n')
    except IOError as IO:
        print(IO)
        print("ERROR!")
    finally:
        for f in file_list:
            f.close()
    print("操作完成！")



if __name__ == '__main__':
    main()