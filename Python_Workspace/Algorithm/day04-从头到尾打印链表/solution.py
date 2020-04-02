

'''
    输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # listNode代表着列表第一个元素
        head = listNode
        curso = head
        temp = []
        while curso != None:
            temp.append(curso.val)
            curso = curso.next
        return temp[::-1]



if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c

    solution = Solution()
    print(solution.printListFromTailToHead(a))