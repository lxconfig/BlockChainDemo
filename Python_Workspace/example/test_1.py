# print('请输入需要排序的序列：')
# list1 = input()
# list_1 = list1.split(" ")
# list_2 = [int(list_1[i]) for i in range(len(list_1))]
# print(list_2)
#
#
# li = list(map(int,input().split()))

def fab():
    a = 0
    b = 1
    print(a)
    for i in range(10):
        a, b = b, a+b
        print(a)

fab()