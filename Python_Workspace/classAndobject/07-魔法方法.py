class Myclass:
    '''一些常用的魔法方法总结'''
    
    num = 1
    def __init__(self):
        self.name = 'sss'

    def __call__(self):
        # 使实例对象可以被作为函数一样调用
        return "__call__ called"
    
    def __str__(self):
        # print(实例对象)，可以输出内容
        return "__str__ called"
    
    def __repr__(self):
        # 直接输入实例对象，可以输出内容
        # 在IDE中好像无效
        return "__repr__ called"
    
    # 实现这两个方法可以创建一个上下文管理器
    # def __enter__(self):
    #     pass
    # def __exit__(self):
    #     pass
    
    

if __name__ == "__main__":
    myclass = Myclass()
    print(myclass())
    print(myclass)
    print(Myclass.__doc__)    # 输出类或函数的描述信息(即包含在三个引号中的内容)
    print(myclass.__class__)  # 输出创建实例对象的类
    print(myclass.__dict__)   # 输出实例对象的所有属性(必须在__init__中初始化的)
    print(Myclass.__dict__)   # 输出类的所有属性和方法

