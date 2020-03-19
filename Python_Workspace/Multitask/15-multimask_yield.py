import time


def task1():
    while True:
        print("---1---")
        time.sleep(1)
        yield


def task2():
    while True:
        print("---2---")
        time.sleep(1)
        yield


def main():
    """
        用生成器yield实现多任务
    """
    # 创建两个生成器对象    
    t1 = task1()
    t2 = task2()

    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()