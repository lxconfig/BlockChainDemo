from multiprocessing import Pool
import time
import os, random


def worker(i):
    start = time.time()
    print("%s开始执行,进程号为%d" % (i, os.getpid()))
    # random.random()随机生成0-1的浮点数
    time.sleep(random.random() * 2)
    stop = time.time()
    print(i, "执行完毕,耗时%0.2f" % (stop - start))


def main():
    """
        创建进程池
    """
    # 创建进程池，设置池中包含3个进程(此时还没有创建进程)
    p = Pool(3)

    for i in range(10):
        # 传递任务函数给进程池中的进程
        # apply_async(任务函数, (共享变量,))
        p.apply_async(worker, (i,))

    # 关闭进程池
    p.close()
    # 等待进程池中的进程结束(与进程和线程不同，进程池不会等待其中的进程结束再结束)
    # 必须放在close()后面
    p.join()


if __name__ == "__main__":
    print("---start---")
    main()
    print("---end---")