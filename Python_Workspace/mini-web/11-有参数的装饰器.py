def main(): 
    '''
        带有参数的装饰器
    '''
def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print('---level 1---')
            elif level_num == 2:
                print('---level 2---')
            return func()
        return call_func
    return set_func


# 等价于两个步骤：
# 1. 先调用set_level函数，并将1作为参数
# 2. 将set_level的返回值(函数引用)配合@符号一起当作装饰器，开始对test进行装饰
@set_level(1)
def test(): 
    print("---test---")
    return 'ok'

print(test())

if __name__ == "__main__":
    main()