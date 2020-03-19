

def main():
    '''
        数字字符转为数字列表
    '''
    a = '3441241'
    b = list(map(int, a))
    print(b)

    # 列表推导式
    c = [int(i) for i in a]
    print(c)


if __name__ == "__main__":
    main()