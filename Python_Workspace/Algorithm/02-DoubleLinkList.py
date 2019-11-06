# -*- coding:utf-8 -*-
# time: 2019/8/14 13:46
# File: 02-DoubleLinkList.py


class Node:
    """节点类"""
    def __init__(self, element):
        self.element = element
        self.prev = None
        self.next = None


class DoubleLinkList:
    """双链表"""
    def __init__(self, node=None):
        """创建头节点"""
        self._header = node

    def is_empty(self):
        """判空"""
        return self._header == None

    def length(self):
        """双链表长度"""
        cur = self._header
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历双链表"""
        if self.is_empty():
          print("双链表中没有元素")
        else:
            cur = self._header
            while cur:
                print(cur.element, end=" ")
                cur = cur.next
        print()

    def append(self, item):
        """尾插法"""
        node = Node(item)
        if self.is_empty():
            self._header = node
            # print("尾部插入完成")
        else:
            cur = self._header
            while cur.next:
                cur = cur.next
            cur.next = node
            node_prev = cur
            # print("尾部插入完成")

    def add(self, item):
        """头插法"""
        node = Node(item)
        if self.is_empty():
            self._header = node
            # print("头部插入成功")
        else:
            cur = self._header
            node.next = cur
            cur.prev = node
            self._header = node # 头指针始终指向第一个元素
            # print("头部插入成功")

    def insert(self, pos, item):
        """指定位置插入元素"""
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            if self.is_empty(): # 索引位置正常，但双链表为空
                self._header = node
            else:
                index = 0
                cur = self._header
                prior = None
                while index < pos:
                    index += 1
                    prior = cur
                    cur = cur.next
                node.next = cur  # 有多种写法
                cur.prev = node
                prior.next = node
                node.prev = prior


    def search(self, item):
        if self.is_empty():
            print("双链表中没有%s这个元素" % item)
        else:
            cur = self._header
            index = 0
            try:
                while cur.element != item:
                    index += 1
                    cur = cur.next
            except AttributeError:
                print("双链表中没有%s这个元素" % item)
            else:
                print("%s是双链表的第%s个元素" % (item, index))

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            print("双链表为空，无法删除元素")
        else:
            cur = self._header
            prior = None
            try:
                while cur.element != item:
                    prior = cur
                    cur = cur.next
            except AttributeError:
                print("双链表中没有%s这个元素，无法删除" % item)
            else:
                if cur == self._header: # 判断删除的是不是第一个元素
                    self._header = cur.next
                    if cur.next: # 防止只有一个元素
                        cur.next.prev = None
                else:
                    prior.next = cur.next
                    if cur.next:
                        cur.next.prev = prior

if __name__ == '__main__':
    Double_link_list = DoubleLinkList()
    # print(Double_link_list.is_empty())
    # print(Double_link_list.length())
    # Double_link_list.travel()

    # Double_link_list.append(1)
    # Double_link_list.append(2)
    # Double_link_list.append(3)

    Double_link_list.add(1)
    Double_link_list.add(2)
    Double_link_list.travel()

    Double_link_list.insert(-3, 3)
    Double_link_list.travel()
    Double_link_list.insert(10, 0)
    Double_link_list.travel()
    Double_link_list.insert(2, -1)
    Double_link_list.travel()

    # Double_link_list.search(-1)
    # Double_link_list.search(3)
    # Double_link_list.search(0)

    Double_link_list.remove(3)
    Double_link_list.travel()
    Double_link_list.remove(0)
    Double_link_list.travel()
    Double_link_list.remove(-1)
    Double_link_list.travel()
    Double_link_list.remove(4)
    Double_link_list.travel()
