# -*- coding:utf-8 -*-
# time:2018/12/11

def c2f(t):
    fac = t * 1.8 + 32
    return fac

def f2c(t):
    c = (t - 32) / 1.8
    return c

def test():
    print("测试，0摄氏度 = %.2f华氏度" % c2f(0))
    print("测试，0华氏度 = %.2f摄氏度" % c2f(0))
if __name__ == "__main__":
    test()
