
def main():
    '''
        用type动态创建一个类
    '''
    # 通常type的使用方式是判断一个变量的类型
    a = type('ooo')
    print(a)

    # 实际上，type本身是一个类，除了上面的用法外，还可以用来创建类
    # type(类名, (类的父类名,), {类的属性})
    b = type("Myclass", (), {"num": 100, "name": "张三"})
    # 返回值是一个类
    print(b)
    c = b()
    print(c.name)
    
    # print(globals())


if __name__ == "__main__":
    main()