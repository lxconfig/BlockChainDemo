def d1(func):
    print("---d1---")
    def call_func(*args, **kwargs):
        print("---d1 call_func---")
        return func(*args, **kwargs)
    return call_func


def d2(func):
    print("---d2---")
    def call_func(*args, **kwargs):
        print("---d2 call_func---")
        return func(*args, **kwargs)
    return call_func


# 装饰器下面一定要是函数才能装饰
# 多个装饰器的顺序：
# 装饰时(进入装饰器)从下向上，执行时(进入装饰器内部函数)从上向下
# 简单来说 谁在前就先执行谁
# test-->d1.call_func   d1.func-->d2.call_func   d2.func-->test
@d1  # 等价于  test = d1(test)
@d2  # 等价于  test = d2(test)
def test():
    print('---test---')


test()