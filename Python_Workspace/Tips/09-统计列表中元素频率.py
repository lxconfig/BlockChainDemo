from collections import Counter


def main():
    '''
        统计列表中某个元素的出现频率，并找到频率最高的元素
    '''
    a = ['q', 'e', 'q', 'w', 'tr', 'df', 'r', 'q', 'r']
    b = dict()
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    
    print(max(b, key=lambda x: b[x]))

    # 或
    count = Counter(a)
    print(count)
    print(count['e'])
    # 按出现频率排列成一个列表，第一个元素就是频率最高的元素
    # [('q', 3), ('r', 2), ('e', 1), ('w', 1), ('tr', 1), ('df', 1)]
    print(count.most_common())

    # Counter还可以用来判断字符串中的元素是否相同
    # 不管顺序，只看元素和数量
    c, d = 'qwe', 'ewq'
    cc, dd = Counter(c), Counter(d)
    if cc == dd:
        print('c与d元素相同')

if __name__ == "__main__":
    main()