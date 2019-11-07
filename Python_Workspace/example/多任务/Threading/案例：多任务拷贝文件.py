# -*- coding:utf-8 -*-
# time: 2019/05/12 14:04
# File: 案例：多任务拷贝文件.py
"""
1.创建多进程（进程池）来完成拷贝
2.显示拷贝进度条（进程间的通信-队列）
"""
import os
import multiprocessing

def copy_data(file_name, waited_copy_file, new_file, queue):
    old_file_path = waited_copy_file + "/" + file_name
    new_file_path = new_file + "/" + file_name
    with open(old_file_path, 'rb') as f:
        content = f.read()
    with open(new_file_path, 'wb') as fp:
        fp.write(content)
    # 拷贝完成一个文件，则将文件名写入队列中
    if not queue.full():
        queue.put(file_name)


def main():
    # 输入要拷贝的文件夹
    waited_copy_file = input("请输入要拷贝的文件夹：")
    # 遍历此文件夹中的文件
    file_list = os.listdir(waited_copy_file)
    old_file_num = len(file_list)  # 获取文件夹中文件的数量
    # 创建新的文件夹来接收拷贝的文件
    new_file = waited_copy_file + "[副本]"
    if not os.path.exists(new_file):
        os.mkdir(new_file)
    # 创建队列
    queue = multiprocessing.Manager().Queue()
    # 创建进程池
    pool = multiprocessing.Pool(5)
    for file_name in file_list:
        pool.apply_async(copy_data, args=(file_name, waited_copy_file, new_file, queue))
    # 结束进程池
    pool.close()
    # 主进程显示进度条百分比
    completed_file_num = 0  # 已经copy完成的文件数
    while True:
        if not queue.empty():
            name = queue.get()
            completed_file_num += 1
            print("\r拷贝进度%.2f%%" % (completed_file_num*100/old_file_num), end="")
            if completed_file_num >= old_file_num:  # 若已拷贝文件数>=待拷贝文件数，则拷贝完成
                break
    print()

if __name__ == '__main__':
    main()