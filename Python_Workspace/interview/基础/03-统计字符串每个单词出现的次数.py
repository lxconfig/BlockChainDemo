# coding:utf-8
# time: 2019/8/27 14:21
# File: 03-统计字符串每个单词出现的次数.py

def main():
    strs = "communication"
    dict1 = {}
    for i in strs:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    return dict1


if __name__ == '__main__':
    print(main())