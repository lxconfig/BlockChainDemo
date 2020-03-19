
def main():
    """
        斐波那契数列
    """
    class Fabonacci():
        def __init__(self, num):
            self.num = num
            self.a = 0
            self.b = 1
            self.current_num = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.current_num < self.num:
                ret = self.a
                self.a, self.b = self.b, self.a + self.b
                self.current_num += 1
                return ret
            else:
                raise StopIteration
    
    fabonacci = Fabonacci(10)
    for i in fabonacci:
        print(i)


if __name__ == "__main__":
    main()