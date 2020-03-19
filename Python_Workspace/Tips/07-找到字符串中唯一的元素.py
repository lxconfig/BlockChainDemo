

def main():
    '''
        返回字符串中的字符,相同的只返回一次
    '''
    a = 'qwrretqteqerqretew'
    b = ''.join((set(a)))
    print(b)

    # 检查唯一性
    c = set(a)
    if len(c) == len(a):
        print("a中的元素是唯一的")
    else:
        print("a中的元素不是唯一的")

    d = ''.join([i for i in a])
    print(d)

if __name__ == "__main__":
    main()