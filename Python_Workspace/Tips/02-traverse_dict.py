

def main():
    """
        遍历字典
    """
    x = {"张三": 33, "李四": 32}

    # items()函数将字典转变为元组
    # dict_items([('张三', 33), ('李四', 32)])
    print(x.items())
    for key, value in x.items():
        print(key + ":" + str(value))


if __name__ == "__main__":
    main()