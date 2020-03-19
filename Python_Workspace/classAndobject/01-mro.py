class Parent:
    def __init__(self, name, *args):
        print("---parent init---")
        self.name = name
        print("---parent init over---")


class son(Parent):
    def __init__(self, name, age, *args):
        print("---son init---")
        self.age = age
        super().__init__(name, *args)
        print("---son init over---")


class daughter(Parent):
    def __init__(self, name, gender, *args):
        print("---daughter init---")
        self.gender = gender
        super().__init__(name, *args)
        print("---daughter init over---")


class friend(son, daughter):
    def __init__(self, name, age, gender):
        print("---friend init---")
        super().__init__(name, age, gender)
        print("---friend init over---")


if __name__ == "__main__":
    a = friend('xiaoming', 8, 'male')
    # 多继承时，super()方法的执行顺序是按照__mro__属性的值(C3算法决定)来执行的
    # 多继承需要传递全部参数
    print(friend.__mro__)
    print(a.name, a.age, a.gender)