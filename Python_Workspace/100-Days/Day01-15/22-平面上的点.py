# -*- coding:utf-8 -*-
# time: 2019/8/8 16:13
# File: 22-平面上的点.py

import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_point(self, dx, dy):
        """
        移动指定的增量
        :param dx: x方向增量
        :param dy: y方向增量
        """
        self.x += dx
        self.y += dy
        return self.x, self.y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 指定位置的x坐标
        :param y: 指定位置的y坐标
        """
        self.x = x
        self.y = y
        return self.x, self.y

    def calc_distance(self, other):
        """
        计算两点距离
        :param other: 另一个点
        :return: 距离
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        """
        print(p1, p2)能直接输出结果
        """
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(10, 20)
    p2 = Point(39, 9)
    print(p1, p2)
    print(p1.calc_distance(p2))

    print(p1.move_point(-2, -4))
    print(p2.move_to(19, 34))
    print(p1.calc_distance(p2))


if __name__ == '__main__':
    main()
