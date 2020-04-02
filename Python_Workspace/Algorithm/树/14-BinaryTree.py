# coding:utf-8
# time: 2019/8/27 9:23
# File: 14-BinaryTree.py

class Node:
    def __init__(self, element):
        self.element = element
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.lchild:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if not cur_node.rchild:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)


    def Breadth_travel(self):
        """广度优先遍历"""
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.element, end=" ")
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)

    def PreOrder(self, root):
        """先序遍历"""
        if not root:
            return
        print(root.element, end=" ")
        self.PreOrder(root.lchild)
        self.PreOrder(root.rchild)

    def InOrder(self, root):
        """中序遍历"""
        if not root:
            return
        self.InOrder(root.lchild)
        print(root.element, end=" ")
        self.InOrder(root.rchild)

    def PostOrder(self, root):
        """后序遍历"""
        if not root:
            return
        self.PostOrder(root.lchild)
        self.PostOrder(root.rchild)
        print(root.element, end=" ")

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.Breadth_travel()
    print()
    tree.PreOrder(tree.root)
    print()
    tree.InOrder(tree.root)
    print()
    tree.PostOrder(tree.root)