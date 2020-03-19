def set_func(func):
    def call_func(*args, **kwargs):
        print("---call_func---")
        # 拆包，将args和kwargs中的每个值作为参数传递
        # 不能写成func(args, kwargs) 这样是传递两个参数: 一个元组，一个字典
        func(*args, **kwargs)
    return call_func


@set_func
def test(num, *args, **kwargs):
    print('---test---%d' % num)
    print('---test---', args)
    print('---test---', kwargs)



test(100)
test(100, 200, 300)
test(100, t=1, r=3)

