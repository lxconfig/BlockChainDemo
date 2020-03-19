import re


def add(temp):
    rest = temp.group()
    change_rest = int(rest) * 10
    return str(change_rest)


def main():
    """
        1. match(r"", 字符串y)
            - 从头匹配

        2. search(r"", 字符串y)
            - 只要在字符串中匹配到字符就输出(只输出第一个字符)

        3. findall(r"", 字符串y)
            - 跟search()类似，但是会把匹配到的全部输出成一个列表

        4. sub(r"", 字符串x, 待匹配的字符串y)
            - 根据正则表达式去y中匹配，将匹配到的部分替换成x
            - x还可以是一个函数，会将匹配得到的对象作为参数传递
            - 不会改变原字符串y

        5. split(r"", 字符串y)
            - 根据正则表达式对y进行切割，输出一个列表
    """

    chats = "python=9998, java=3525, c++=5642"

    ret1 = re.search(r"\d+", chats).group()
    print("search()方法的结果:", ret1)

    ret2 = re.findall(r"\d+", chats)
    print("findall()方法的结果:", ret2)

    ret3 = re.sub(r'\d+', "1234", chats)
    print("sub()方法的结果:", ret3)
    # print(chats)

    ret4 = re.sub(r'\d+', add, chats)
    print("sub()方法调用函数的结果:", ret4)

    ret5 = re.split(r", ", chats)
    print("split()方法的结果:", ret5)


if __name__ == "__main__":
    main()