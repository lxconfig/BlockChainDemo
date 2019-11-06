# -*- coding:utf-8 -*-
# time: 2019/8/9 10:06
# File: 23-限定类对象只绑定某些属性.py


class Person:
    __slots__ = ("_name", "_age", "_gender")  # 绑定属性

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 18:
            print("%s正在玩飞行棋" % self._name)
        else:
            print("%s正在玩斗地主" % self._name)

def main():
    person = Person("王大锤", 22)
    person.play()
    person.age = 11  # 实际上调用了age(self, age)
    person.play()
    person._gender = "男"

if __name__ == '__main__':
    main()