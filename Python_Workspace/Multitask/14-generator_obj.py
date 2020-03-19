
"""
总结:
    1. 生成器是一种特殊的迭代器

    2. 函数中只要包含yield关键字，那么就称这个函数是生成器的"模板"

    3. 在调用包含yield关键字的函数"模板"时，不会调用这个函数，而是会创建一个生成器对象

    4. 两种启动生成器的方法:
        - next(generator_obj)
        - generator_obj.send(parameter)
        
    5. 创建生成器的两种方法:
        - 定义函数，使用yield关键字
        - 将列表推导式的 [] 换成 (), 例: obj = (i for i in range(10))
"""


def main(num):
    """
        生成器对象
    """
    print("--1--")
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        print("--2--")
        # 程序每次执行到yield时，会将a的值传递给for循环打印，之后就返回for循环开始下一次
        # 在下一次循环中，不会再从头开始执行，而是从yield后的语句开始执行
        # temp = yield a 是两条语句，send传递过来的参数作为yield的返回值
        temp = yield a
        print(temp)
        print("--3--")
        a, b = b, a+b
        current_num += 1
        print("--4--")


if __name__ == "__main__":
    generator_obj = main(2)
    # for i in generator_obj:
    #     print(i)

    ret = next(generator_obj)
    print(ret)


    # 取不到值时，报错: StopIteration
    # ret = next(generator_obj)
    # print(ret)

    # 另一种启动生成器的方式: send()
    # 可以给生成器传递参数，即作为yield a的返回值
    # send尽量不要放在第一次调用，因为没有变量接收参数(除非传递None)
    ret = generator_obj.send("hhh")
    print(ret)