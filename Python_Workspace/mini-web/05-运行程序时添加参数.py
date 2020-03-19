import sys


def main():
    '''
        在终端运行命令时，添加一些参数运行
    '''
    # sys.argv能够得到在终端输入的内容，并保存成一个列表(不包含python3)
    parameters = sys.argv
    print(parameters)

    # 导入模块的另一种方法
    # import a 不会将a看作变量解析，而是直接导入a.py
    # 相反__import__(a) 会将a看作变量解析，再导入a指向的值
    # 返回值ret标记着这个导入的模块
    ret = __import__(parameters[1])
    print(ret)

    # getattr(模块, 模块中的某个函数)，返回此函数的引用
    # <function application at 0x000001F16E461510>
    app = getattr(ret, 'application')
    print(app)

if __name__ == "__main__":
    main()