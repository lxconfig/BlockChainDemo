import re


def main():
    """
        匹配邮箱地址，要求@符号前有4-20位数字或字母
    """
    email_addrs = ["hello@163.com", "wr@163.com", "163.com", "@163.com", "aef@!@163.com", "segweg_were@163.com"]

    for addr in email_addrs:
        try:
            # $判断结尾: 字符和正则正好匹配完
            # \转义
            print("匹配出来的结果:", re.match(r'^[0-9a-zA-Z_]{4,20}@163\.com$', addr).group())
        except Exception:
            print("邮箱不合法:", addr)




if __name__ == "__main__":
    main()