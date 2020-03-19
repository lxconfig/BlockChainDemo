import os


lines = 0
basedir = '/home/lixuan/code'


def read_content(file):
    """读取内容"""
    global lines
    with open(file, 'rb') as f:
        count = len(f.readlines())
        lines += count
    print(file + '----  %d' % count)


def read_all_files():
    """读取全部文件"""
    for path, dirname, files in os.walk(basedir):
        if path == basedir + '/Multitask/copy_test':
            continue
        for file in files:
            if file.endswith('.py'):
                read_content(os.path.join(path, file))


def main():
    """统计代码行数"""
    os.chdir(basedir)
    # 遍历basedir路径下的全部文件，有文件夹则递归
    read_all_files()


if __name__ == "__main__":
    main()
    print("总行数为:",lines)