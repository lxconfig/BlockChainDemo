import threading
import time


def test1(num):
    global nums
    # 上锁,再释放锁之前,其他线程的上锁操作都将被阻塞
    mutex.acquire()
    for _ in range(num):
        nums += 1
    # 释放锁
    mutex.release()
    print("---in test1 nums=%d" % nums)


def test2(num):
    global nums
    mutex.acquire()
    for _ in range(num):
        nums += 1
    mutex.release()
    print("---in test2 nums=%d" % nums)


nums = 0

# 定义互斥锁
mutex = threading.Lock()


def main():
    """互斥锁解决资源竞争问题"""
    # 互斥锁可能会产生死锁，可以添加超时时间
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))

    t1.start()
    t2.start()

    time.sleep(1)
    print("---in main nums=%d" % nums)

if __name__ == "__main__":
    main()