def test1():
    x = 100
    def test2():
        # 要修改外部函数的变量x,就加上nonlocal x
        # 要修改全局变量x,就加上global x
        nonlocal x
        print("---1---%d" % x)
        x = 200
        print("---2---%d" % x)
    return test2

t = test1()
t()