import re


def main():
    '''
        字符串拆分与合并
    '''
    a = 'i love python'
    b = 'i, love, python'
    c = '   i love python  '
    g = 'i / love p;ython;;'

    d = a.split()
    e = b.split(', ')
    print(d, e)

    # 去掉字符串两边的字符，默认是空格
    f = c.strip()
    print(f)

    # 合并字符串
    h = ' '.join(re.split(r'\W+', g))
    print(h)

if __name__ == "__main__":
    main()