class Money:
    def __init__(self):
        # 定义私有属性，不允许在类的外部修改、访问
        self.__money = 0

    # 有时候需要用到这个私有属性，一般的方法是定义两个函数 get\set
    # 缺点在于需要知道这两个函数是否要传参
    # 所以改用property属性来完成

    def getMoney(self):
        return self.__money
    
    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("不是数字")
    
    # 定义property属性
    money = property(getMoney, setMoney)



if __name__ == "__main__":
    user = Money()
    print("__money=%d" % user.money)
    user.money = 100
    print("设置后,__money=%d" % user.money)