# coding: utf-8
# time: 2019/9/11 下午5:00
# File: test2.py


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return "--repr-- {0}, {1}".format(self.name, self.print_dob())

    def __str__(self):
        return "--str-- {0}, {1}".format(self.name, self.print_dob())

    def print_dob(self):
        filled_dob = self.dob
        to_fill = 8 - len(self.dob)
        for i in range(to_fill):
            filled_dob = filled_dob + '*'
        return filled_dob

if __name__ == '__main__':
    p = Person("ss","19780808")
    p.dob = p.dob[:-1]
    print(p.dob)
    # p 调用__repr__方法
    # print(p)  调用__str__方法