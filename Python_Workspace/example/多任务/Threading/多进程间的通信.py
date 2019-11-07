# -*- coding:utf-8 -*-
# time: 2019/05/08 20:41
# File: 多进程间的通信.py
from multiprocessing import Queue
import multiprocessing

def download_data(data_queue):
    data = [436,65487,795,2352,9595]
    # 将数据入队
    for i in data:
        data_queue.put(i)
    print("数据下载完毕")

def analysis_data(data_queue):
    # 从队列中取数据分析
    analysised_data = list()
    while True:
        data = data_queue.get()
        analysised_data.append(data)
        if data_queue.empty():
            break
    print("数据分析完毕")
    print(analysised_data)

def main():
    # 创建queue
    data_queue = Queue()
    # 创建两个进程
    p1 = multiprocessing.Process(target=download_data, args=(data_queue, ))
    p2 = multiprocessing.Process(target=analysis_data, args=(data_queue, ))
    # 启动进程
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()