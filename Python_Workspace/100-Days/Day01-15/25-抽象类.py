# -*- coding:utf-8 -*-
# time: 2019/8/9 14:50
# File: 25-抽象类.py

import abc

class Pet(metaclass=abc.ABCMeta):  # 抽象类，不能实例化对象，专门用来被继承
    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print("%s:汪汪汪" % self._name)

class Cat(Pet):
    def make_voice(self):
        print("%s喵喵喵" % self._name)

def main():
    pets = [Dog("xx"), Cat("CC")]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()