class Myclass:
    # property属性: 类似于将方法改装成了属性
    # 被装饰的这个方法，除了self外，不能有其他参数
    # 能够被继承,能够被重写
    @property
    def get(self):
        return "aaa"

class son(Myclass):
    # @property
    # def get(self):
    #     return 100
    pass

if __name__ == "__main__":
    myclass = Myclass()

    print(myclass.get)

    s = son()
    print(s.get)