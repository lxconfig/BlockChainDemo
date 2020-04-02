# -*- coding:utf-8 -*-
# time: 2019/8/21 15:16
# File: 05-Queue.py

class Queue:
    def __init__(self):
        self.__item = []
    
    def is_empty(self):
        return self.__item == []
    
    def size(self):
        return len(self.__item)
    
    def push(self, item):
        self.__item.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.__item.pop(0)
        else:
            return None

if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    print(queue.size())
    queue.push(1)
    queue.push(2)
    print(queue.size())
    print(queue.pop())
    print(queue.pop())