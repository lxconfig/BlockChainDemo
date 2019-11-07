# -*- coding:utf-8 -*-
# time: 2019/06/12 18:26
# File: demo2.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        if not l1:
            return l2

        if not l2:
            return l1

        carry = 0
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next

        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                p = p.next

        if carry == 1:
            p.next = ListNode(1)

        # dummy = dummy.next
        # while dummy:
        #     print(dummy.val)
        #     dummy = dummy.next
        return dummy.next


# l1_1 = ListNode(2)
# l1_2 = ListNode(4)
# l1_3 = ListNode(3)
# l1_1.next = l1_2
# l1_2.next = l1_3
#
# l2_1 = ListNode(5)
# l2_2 = ListNode(6)
# l2_3 = ListNode(4)
# l2_1.next = l2_2
# l2_2.next = l2_3
#
# s = Solution()
# s.addTwoNumbers(l1_1, l2_1)

class Solutions:
    def addtwonums(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        temp = ListNode(0)
        res = temp
        carry = 0

        while l1 and l2:
            temp.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1, l2, temp = l1.next, l2.next, temp.next

        if l1:
            while l1:
                temp.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1, temp = l1.next, temp.next

        if l2:
            while l2:
                temp.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2, temp = l2.next, temp.next

        if carry == 1:
            temp.next = ListNode(1)


        res = res.next
        while res:
            print(res.val)
            res = res.next
        # return res.next
l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

s = Solutions()
s.addtwonums(l1_1, l2_1)