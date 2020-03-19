class Myclass:
    gender = 'male'
    _x = 10    # 私有化属性，禁止被导入，但是类和子类可以访问
    __x = 100  # 避免与子类的属性名重复，无法再外部访问，子类无法访问 (找不到是因为把名字改了 __x --> _Myclass__x,即名字重整)

    def __init__(self, name):
        self.name = name
        # self.__x = Myclass.__x

    # 类方法，不需要传入实例对象self,而需要类对象cls
    @classmethod
    def set_gender(cls, gender):
        cls.gender = gender
        print(cls.gender)


    # 静态方法，不需要传入self或cls
    @staticmethod
    def show_gender():
        print(Myclass.gender)


class son(Myclass):
    pass


if __name__ == "__main__":
    # 静态方法不需要实例化就能调用
    '''
    Myclass.show_gender()
    # 类方法也不需要实例化就能调用
    Myclass.set_gender("Unknow")

    myclass = Myclass('zhangsan')
    # 实例对象可以访问：类属性，类方法，静态方法
    print(myclass.gender)
    myclass.set_gender('fmale')
    myclass.show_gender()
    '''

    # 类方法、静态方法、类属性能够被继承
    '''
    s = son('lisi')
    print(s.gender)
    s.set_gender("fmale")
    s.show_gender()
    '''
    