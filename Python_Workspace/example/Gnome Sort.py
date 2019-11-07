def Gnome():
    i = 0
    print('请输入需要排序的序列：')
    list1 = list(map(int,input().split(",")))
    while (i < len(list1)):
        if (i == 0 or list1[i-1] <= list1[i]):
            i += 1
        else:
            temp = list1[i]
            list1[i] = list1[i-1]
            list1[i-1] = temp
            i -= 1
    return list1
