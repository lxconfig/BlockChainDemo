import threading
import time

def test1():
    for _ in range(5):
        print("---test1---")


def test2():
    for _ in range(5):
        print("---test2---")


def main():
    """通过target指定任务函数，创建线程"""
    # 创建线程
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    # 启动线程
    # 只有在调用start()方法之后，创建的子线程才真正开始执行
    t1.start()
    time.sleep(1)
    t2.start()

    # 查看线程数量
    print(threading.enumerate())


if __name__ == "__main__":
    main()