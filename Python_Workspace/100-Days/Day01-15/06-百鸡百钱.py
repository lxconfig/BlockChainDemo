# -*- coding:utf-8 -*-
# time: 2019/7/31 15:31
# File: 06-百鸡百钱.py

# 百鸡百钱：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

def calc_num(money):
    # 5x + 3y + (100-x-y)/3 = 100元  ->  14x + 8y = 200

    for x in range(0, 20):
        for y in range(0, 34):
            if 14 * x + 8 * y == 200:
                print("公鸡%d只，母鸡%d只，小鸡%d只" % (x, y, (100-x-y)))


if __name__ == '__main__':
    calc_num(100)