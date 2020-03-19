import re


def main():
    """
        使用分组，检查html标签是否配对
    """
    html_tags = [
        "<h1>sss</h1>",
        "<option>sgsg</option>",
        "<h1>dsg</h3>",
        "<select>dsg</body>",
        "<body><h1>sgsdga</h1></body>"
    ]

    for tag in html_tags:
        try:
            # ()能够将数据分组, 可以直接用1,2...取到分组的数据  group(1)
            # 还能够在正则表达式中写\1, 前提是之前有分组
            # (?P<分组名>)  (?P=分组名)
            # 匹配嵌套标签
            # print("匹配成功:", re.match(r"^<(\w*)><(\w*)>.*</\2></\1>$", tag).group())
            print("匹配成功:", re.match(r"^<(\w*)>.*</\1>$", tag).group())
        except Exception:
            print("配对失败:", tag)



if __name__ == "__main__":
    main()