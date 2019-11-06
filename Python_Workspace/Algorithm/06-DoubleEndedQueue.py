# coding:utf-8
# time: 2019/8/21 15:27
# File: 06-DoubleEndedQueue.py

class DoubleEndedQueue:
    def __init__(self):
        self.__item = []

    def is_empty(self):
        return self.__item == []

    def size(self):
        return len(self.__item)

    def push_front(self, item):
        self.__item.insert(0, item)

    def pop_front(self):
        if not self.is_empty():
            return self.__item.pop(0)
        else:
            return None

    def push_rear(self, item):
        self.__item.append(item)

    def pop_rear(self):
        if not self.is_empty():
            return self.__item.pop()
        else:
            return None


if __name__ == '__main__':
    queue = DoubleEndedQueue()

    queue.push_front(1)
    print(queue.pop_front())
    queue.push_rear(2)
    print(queue.pop_rear())
    print(queue.size())

