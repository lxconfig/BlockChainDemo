# -*- coding:utf-8 -*-
# time: 2019/8/9 10:16
# File: 24-静态方法和类方法.py

import math
import time

class Triangle:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod   # 静态方法，通过类名调用此方法，调用时还未生成对象
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return math.sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

class Clock:
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):  # 类方法，带cls(类名)参数，返回一个对象
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print("无法构成三角形")

    clock = Clock.now()
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()

if __name__ == '__main__':
    main()