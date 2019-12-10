# 无参数无返回值的装饰器
def decorate(func):
    def check_login():
        print('----check_login----')
        func()
    return check_login

# 等价于 decorate(login), @的作用是传递函数对象login作为装饰器函数的参数
@decorate
def login():
    print('----login----')

print(type(login))
login()
# 执行过程：
# 1. 调用login()时，发现login被装饰器修饰，则转到装饰器decorate中执行，login作为参数赋值给func
# 2. decorate返回一个函数对象check_login,并调用check_login函数
# 3. 执行check_login函数的逻辑，同时在其中调用了func(),也就是调用了login()

# 有参数无返回值的装饰器
def decorate_para(func):
    def wrapper(b):
        print("----wrapper b is %s----" % b)
        func(b)
    return wrapper

@decorate_para
def set(a):
    print("---set a is %s----" % a)
set(1)
# 执行过程：
# 1. 前面的过程和普通装饰器一样
# 2. 针对参数a,会把它作为wrapper函数的参数，然后调用func()时再传递回set()
# 3. 对于多参数的情况，写法是：wrapper(*args, **kwargs),其中*args表示位置参数，**kwargs表示关键字参数

# 多个参数无返回值的装饰器
def decorate_paras(func):
    def wrapper(*args):   # *args表示位置参数
        print("----wrapper is running...----")
        func(*args)
        print('----wrapper is running over----')
    return wrapper
    # def wrapper(**kwargs):  # *kwargs表示关键字参数
    #     print("----wrapper is running...----")
    #     func(**kwargs)
    #     print('----wrapper is running over----')
    # return wrapper

@decorate_paras
def set_list(a,b,c,d):
    print('----set_list is %s' % [a,b,c,d])
set_list(1,2,3,4)  # 位置参数调用
# set_list(a=1,b=2,c=3,d=4)  # 关键字参数调用

# 无参数有返回值的装饰器
def decorate_return(func):
    def wrapper():
        print('----wrapper is running----')
        return func()
    return wrapper

@decorate_return
def add():
    return 'a + b = 10'
print(add())
# 执行过程：
# 1. 前面的过程和普通装饰器一样
# 2. 对于被装饰函数的返回值，只要在wrapper()中调用它时，返回就行

# 有参数有返回值的装饰器
def decorate_paras_return(func):
    def wrapper(*args):
        print('----wrapper is running----')
        return func(*args)
    return wrapper

@decorate_paras_return
def sum(a, b):
    return '%s + % s = %s' % (a, b, a+b)

print(sum(3,6))