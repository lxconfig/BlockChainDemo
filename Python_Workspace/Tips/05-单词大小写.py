

def main():
    '''
        单词大小写
        三个函数都不是原地修改
    '''
    a = 'i love python.'
    # 单词首字母大写
    b = a.title()
    # print(id(a), id(a.title()))
    print(b)

    # 所有字母大写
    c = a.upper()
    # print(id(a), id(a.upper()))
    print(c)

    # 字符串首字母大写
    d = a.capitalize()
    # print(id(a), id(d))
    print(d)



if __name__ == "__main__":
    main()