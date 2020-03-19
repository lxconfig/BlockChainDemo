'''
    创建property属性的方法:
    1. 装饰器的方法
        @property
        @property.setter
        @property.deleter

    2. 通过property类  a = property(func_name)
        property(fget, fset, fdel, doc)
            fget: 即获取属性的值, 在myclass.num时调用
            fset: 即设置属性的值, 在myclass.num=100时调用
            fdel: 即删除属性的值, 在del myclass.num时调用
            doc:  字符串，获取该属性的描述信息, 在Myclass.num.__doc__时调用 (类名.属性名.__doc__)
'''

class Myclass:
    num = 1
    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    # 获取property属性的值
    # 此时写的函数名price，之后设置、删除时也要写price    
    @property
    def price(self):
        return self.original_price

    # 设置property属性的值
    @price.setter
    def price(self, value):
        self.original_price = value

    # 删除property属性的值
    @price.deleter
    def price(self):
        del self.original_price

    # 定义普通的实例方法
    def get(self):
        return Myclass.num
    def set(self, value):
        Myclass.num = value
    def delete(self):
        del Myclass.num

    # 通过property类创建property属性
    pro = property(get, set, delete, 'num属性')


if __name__ == "__main__":
    '''
    myclass = Myclass()

    print('商品原价:', myclass.price)
    myclass.price = 200
    print('商品修改后的价格:', myclass.price)

    del myclass.price  # 没有original_price这个属性了
    # print('商品原价:', myclass.price)
    '''
    myclass = Myclass()
    # 会去调用get()方法，获取其返回值
    print(myclass.pro)
    # 调用set()方法，设置num的值
    myclass.pro = 2
    print(myclass.pro)
    # 调用delete()方法，删除num
    # del myclass.pro
    print(Myclass.pro.__doc__)


