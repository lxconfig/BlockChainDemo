from functools import reduce

def main():
    '''字符串翻转'''
    a = 'python'
    b = a[::-1]
    print(b)

    # 或者用reduce函数
    reverse = lambda x,y : y+x
    c = reduce(reverse, a)
    print(c)
    # print(reverse)
    
    # 判断回文串
    d = 'qwewq'
    if d == d[::-1]:
        print('是回文串')
    else:
        print("不是回文串")

if __name__ == "__main__":
    main()