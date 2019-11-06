# -*- coding:utf-8 -*-
# time: 2019/8/21 15:05
# File: 04-Stack.py

class Stack:
    def __init__(self):
        self.__item = []

    def is_empty(self):
        return self.__item == []

    def size(self):
        return len(self.__item)

    def push(self, item):
        self.__item.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.__item.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.__item[0]
        else:
            return None

if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    print(stack.size())
    stack.push(1)
    stack.push(2)
    print(stack.size())
    print(stack.pop())
    print(stack.peek())

