from collections.abc import Iterable, Iterator  # 对象只要是继承自Iterable类，就是可迭代对象

"""
    总结:
    1. 如何判断一个对象是可迭代的对象？
        - 只要这个对象实现了__iter__()方法即可
        - 其中，__iter__()方法需要返回一个迭代器对象
    
    2. 如何判断一个对象是迭代器对象？
        - 只要这个对象实现了__iter__()方法和__next__()方法即可

    3. 迭代器一定可迭代，可迭代不一定是迭代器(不一定包含__next__()方法)

    4. 在类型转换中，也使用到了迭代器(如: list ---> tuple)
"""


def main():
    """
        自定义可迭代的对象
    """
    class ClassMate():
        def __init__(self):
            self.name = list()
        
        def add(self, name):
            self.name.append(name)
        
        def __iter__(self):
            # 一个类只要包含__iter__()方法，那么这个类创建出来的对象就是可迭代的
            # 返回值: 必须返回一个迭代器对象
            return ClassIterator(self)  # 返回ClassIterator类的对象，并且此对象包含__iter__和__next__方法，所以返回的是迭代器对象
            
    class ClassIterator():
        def __init__(self, obj):
            self.obj = obj
            self.num = 0

        def __iter__(self):
            pass

        def __next__(self):
            # 一个类即包含__iter__()和__next__()方法，那么这个类创建出来的对象就是一个迭代器
            if self.num < len(self.obj.name):
                ret = self.obj.name[self.num]
                self.num += 1
                return ret
            else:
                # for循环遇到StopIteration异常会直接停止
                raise StopIteration

    
    classmate = ClassMate()
    classmate.add("x")
    classmate.add('y')
    classmate.add('z')

    # isinstance(obj, cls)可以判断某个对象是否是某个类创建的
    print("classmate是否是可迭代的对象:", isinstance(classmate, Iterable))

    # iter()方法调用的是对象中的__iter__()方法
    class_iterator = iter(classmate)  # 得到ClassIterator类的对象
    print("class_inerator是否是迭代器:", isinstance(class_iterator, Iterator))

    """
    for循环的工作流程:
        1. 判断classmate是否是可迭代的对象(通过isinstance() 或 该对象有__iter__()方法)
        2. 在1成立的前提下，调用iter()函数，得到对象classmate中__iter__()方法的返回值(这个返回值是一个迭代器)
        3. 调用next()函数取对象的值(实际调用的就是迭代器的__next__()方法,它的返回值就是for的输出值)
    """
    for i in classmate:
        print(i)


if __name__ == "__main__":
    main()