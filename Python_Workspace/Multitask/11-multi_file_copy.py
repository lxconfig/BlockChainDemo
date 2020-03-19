import multiprocessing
import os


def copy_file(queue, folder_name, file_name, new_folder_name):
    """
        拷贝文件
    """
    # 打开待拷贝的文件
    # print("文件复制: 从%s文件夹--->%s文件夹,文件名是:%s" % (folder_name, new_folder_name, file_name))
    file_path = folder_name + "/" + file_name
    new_file_path = new_folder_name + "/" + file_name
    with open(file_path, "rb") as f:
        content = f.read()
        with open(new_file_path, "wb") as n:
            n.write(content)
    
    # 拷贝完一个文件后，将文件名添加到队列中
    queue.put(file_name)

def main():
    """
        案例：多任务文件拷贝
    """
    # 获取需要拷贝的文件夹名
    folder_name = input("请输入需要拷贝的文件夹名:")

    # 创建新的文件夹
    # 防止文件夹存在时 mkdir报错
    try:
        new_folder_name = '[新]' + folder_name
        os.mkdir(new_folder_name)
    except:
        pass

    # 读取待拷贝文件夹中的所有文件名
    file_names = os.listdir(folder_name)

    # 创建进程池
    pool = multiprocessing.Pool(5)

    # 创建队列，使得进程池中的进程能和主进程通信
    # 这里要通过Manager()类来创建队列
    queue = multiprocessing.Manager().Queue()

    # 向进程池中提交拷贝任务
    for file_name in file_names:
        pool.apply_async(copy_file, (queue, folder_name, file_name, new_folder_name))

    # 结束进程池
    pool.close()
    # pool.join()

    # 主进程计算拷贝进度
    all_file_nums = len(file_names)  # 获取待拷贝文件总数
    copy_complete_nums = 0           # 已拷贝文件数
    while True:
        file_name = queue.get()
        # print("已经完成拷贝:%s" % file_name)
        copy_complete_nums += 1
        # \r表示回车，即光标回到当前行的开头
        print("\r拷贝进度: %0.2f%%" % (copy_complete_nums * 100 / all_file_nums), end="")
        if copy_complete_nums >= all_file_nums:
            # 所有文件拷贝完成
            break

if __name__ == "__main__":
    main()