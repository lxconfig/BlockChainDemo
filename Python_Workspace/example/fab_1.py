def fab(n):
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else:
        return fab(n-1) + fab(n-2)



def fab1(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('error')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3

result = fab1(40)
if result != -1:
    print(result)


def hanoi(n,x,y,z):
    if n == 1:
        print(x ,'-->', z)
    else:
        hanoi(n-1,x,z,y)
        print(x ,'-->', z)
        hanoi(n-1,y,x,z)
