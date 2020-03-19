import multiprocessing

def test1(q):
    # 向队列中写入数据
    data = [3252,6346,23426,234262,3462,236]
    for temp in data:
        # put()写入队列
        q.put(temp)
    print('写入完成')


def test2(q):
    # 从队列中读出数据
    datas = []
    while True:
        # get()读取数据
        datas.append(q.get())
        # empty()判空   full()判满
        if q.empty():
            break
    print(datas)

def main():
    """
        通过队列完成进程间的数据共享
        此外还有其他方法实现: 套接字、文件等
    """
    # 创建队列(可指定队列大小)
    q = multiprocessing.Queue()

    # 创建进程
    p1 = multiprocessing.Process(target=test1, args=(q,))
    p2 = multiprocessing.Process(target=test2, args=(q,))

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()