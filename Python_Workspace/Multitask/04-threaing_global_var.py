import threading
import time

num = 121

def test1():
    global num
    num += 1
    print("---in test1 num=%d" % num)


def test2():
    print("---in test2 num=%d" % num)


def main():
    """验证线程之间共享全局变量"""
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main thread num=%d" % num)

if __name__ == "__main__":
    main()


