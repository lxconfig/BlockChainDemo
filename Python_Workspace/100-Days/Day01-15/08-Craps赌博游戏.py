# -*- coding:utf-8 -*-
# time: 2019/7/31 15:50
# File: 08-Craps赌博游戏.py

"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""

import random

def craps():
    chips = 1000
    while chips > 0:
        print("你的总筹码为：", chips)
        go_on = False
        while True:
            debt = int(input("请下注："))
            if 0 < debt <= chips:
                break
        first_sum = random.randint(1, 6) + random.randint(1, 6)
        print('玩家摇出了%d点' % first_sum)
        if first_sum == 7 or first_sum == 11:
            print("你赢了!")
            chips += debt
        elif first_sum == 2 or first_sum == 3 or first_sum == 12:
            print("你输了!")
            chips -= debt
        else:
            print("平局!")
            go_on = True
        while go_on:
            second_sum = random.randint(1, 6) + random.randint(1, 6)
            print('玩家摇出了%d点' % second_sum)
            if second_sum == 7:
                print("你输了!")
                chips -= debt
                go_on = False
            elif second_sum == first_sum:
                print("你赢了!")
                chips += debt
                go_on = False
            else:
                print("平局！")
                go_on = True
    print("你破产了！游戏结束！")

if __name__ == '__main__':
    craps()