import multiprocessing


def test1():
    while True:
        print("---test1---")


def test2():
    while True:
        print("---test2---")


def main():
    """通过进程实现多任务"""
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    # 启动进程
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()