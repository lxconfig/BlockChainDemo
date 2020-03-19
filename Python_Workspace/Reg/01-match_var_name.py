import re


def main():
    """
        用正则表达式判断变量名是否合法
    """
    var_name = ["name1", "_name", "2_name", "__name__", "name!"]

    for name in var_name:
        try:
            print("合法变量名:", re.match(r"^[a-zA-Z_]\w*$", name).group())
        except Exception:
            print("非法变量名:", name)
        

if __name__ == "__main__":
    main()