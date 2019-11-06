# -*- coding:utf-8 -*-
# time: 2019/8/8 15:54
# File: 21-定义时钟.py

import time

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
            if self.hour == 24:
                self.hour = 0

    def show(self):
        print("%0.2d:%0.2d:%0.2d" % (self.hour, self.minute, self.second))



if __name__ == '__main__':
    clock = Clock(0, 0, 0)
    while True:
        clock.run()
        time.sleep(1)
        clock.show()