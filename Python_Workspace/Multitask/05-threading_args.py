import threading
import time


def test1(temp):
    # 要接收传递的全局变量
    temp.append(431)
    print("---in test1 temp=%s---" % str(temp))


def test2(temp):
    # 要接收传递的全局变量
    print("---in test2 temp=%s---" % str(temp))

nums = [11, 22]

def main():
    """利用args参数完成全局变量的共享"""
    # args要传入一个元组
    t1 = threading.Thread(target=test1, args=(nums,))
    t2 = threading.Thread(target=test2, args=(nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main thread nums=%s" % str(nums))


if __name__ == "__main__":
    main()

