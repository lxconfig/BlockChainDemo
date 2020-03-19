class Parent:
    x = 1


class son(Parent):
    pass


class daughter(Parent):
    pass


if __name__ == "__main__":
    # 继承父类的类属性：实际上是, 子类中创建一个同名变量，同时指向父类的类属性
    # 本例中三个x都指向同一个内存空间
    # python中，类变量是作为字典处理的，如果在当前类中没有发现，则去父类中找，都没找到就报错

    # 1 1 1
    print(Parent.x, son.x, daughter.x)
    print('-'*20)

    son.x = 2
    # 1 2 1
    print(Parent.x, son.x, daughter.x)
    print('-'*20)

    Parent.x = 3
    # 3 2 3
    print(Parent.x, son.x, daughter.x)