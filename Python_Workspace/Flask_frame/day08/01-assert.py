

def div(a, b):
    # assert 断言  跟一个表达式
    # 既我认为程序运行到这，表达式应该返回为true
    # 如果返回为true，则程序继续执行，如果返回为false，则assert会抛出异常AssertionError，并终止程序运行
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert b != 0

    print(a // b)


if __name__ == "__main__":
    # div(1, 0)  # AssertionError
    # div('a', 'b')  # AssertionError
    div(100 ,50)