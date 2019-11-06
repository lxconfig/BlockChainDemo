# -*- coding:utf-8 -*-
# time: 2019/8/12 15:44
# File: 01-SingleLinkList.py

class Node:
    """
    节点类，定义节点元素值以及下一个元素位置
    """
    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkList:
    """
    单链表类
    """
    def __init__(self, node=None):
        self._header = node

    def is_empty(self):
        """
        判断单链表是否为空
        """
        return self._header == None

    def length(self):
        """
        单链表长度
        """
        cur = self._header
        count = 0
        while cur: # cur != None
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历单链表
        """
        cur = self._header
        while cur:
            print(cur.element, end=" ")
            cur = cur.next
        print() # 让下一个输出换行

    def append(self, item):
        """
        单链表尾部添加元素
        :param item: 待添加元素的值
        """
        node = Node(item)
        if self.is_empty():
            self._header = node
        else:
            cur = self._header
            while cur.next:
                cur = cur.next
            cur.next = node

    def add(self, item):
        """
        单链表头部添加元素
        :param item: 待添加的元素值
        """
        node = Node(item)
        node.next = self._header
        self._header = node

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos: 位置
        :param item: 元素值
        """
        if pos <= 0:
            self.add(item)
            print("插入完成")
        elif pos > self.length() - 1:
            self.append(item)
            print("插入完成")
        else:
            node = Node(item)
            count = 0
            cur = self._header
            while cur:
                if count == pos - 1:
                    node.next = cur.next
                    cur.next = node
                    break
                count += 1
                cur = cur.next
            print("插入完成")

    def search(self, item):
        """
        查找节点是否存在
        :param item: 待查找的节点值
        :return index: 带查找节点的索引
        """
        cur = self._header
        index = 0
        try:
            while cur.element != item:
                index += 1
                cur = cur.next
        except AttributeError as a:
            # print(a) # 输出错误信息
            return "单链表中没有%s这个元素" % item
        else:
            return index

    def remove(self, item):
        """
        删除节点（找到的第一个节点）
        :param item: 待删除的节点值
        """
        cur = self._header
        pre = None
        if not cur:
            print("要删除的元素不存在")
        while cur:
            if cur.element != item:
                pre = cur
                cur = cur.next
                if not cur:
                    print("要删除的元素不存在")
            else:
                if cur == self._header:  # 第一个节点就是要删除的元素
                    self._header = cur.next
                else:
                    pre.next = cur.next
                break


if __name__ == '__main__':
    Single_link_list = SingleLinkList()

    Single_link_list.append(1)
    Single_link_list.append(2)
    Single_link_list.append(3)
    Single_link_list.add(4)
    Single_link_list.add(5)
    Single_link_list.add(1)
    print(Single_link_list.length())
    Single_link_list.travel()
    print(Single_link_list.search(5))

    Single_link_list.insert(3, 10)
    Single_link_list.travel()

    Single_link_list.remove(5)
    Single_link_list.travel()

    # Single_link_list.remove(1)
    # Single_link_list.travel()
    #
    # Single_link_list.remove(3)
    # Single_link_list.travel()