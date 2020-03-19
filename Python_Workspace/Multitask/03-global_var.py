
num = [11,42,25]


def test1():
    num.append(3333)

def test2():
    """如果修改了变量的指向，则要加global说明"""
    """仅仅修改变量的值，不需要加"""
    global num
    num += [352,657]

print(id(num))

test2()

print(id(num))

