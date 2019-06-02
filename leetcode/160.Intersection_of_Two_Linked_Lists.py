# https://leetcode.com/problems/intersection-of-two-linked-lists/
# 两个链表如果有交叉的话，后面重合的部分一样是一样长度的。
# 所以首先遍历到两个链表一样长度的地方，然后两个链表同时前向遍历
# 判断是否有一样，一样就停止返回

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        len_b = 0
        l_a = headA
        l_b = headB
        while l_a is not None:
            len_a += 1
            l_a = l_a.next
        while l_b is not None:
            len_b += 1
            l_b = l_b.next
        # 走到两个链表一样的地方
        # 也可以写一个判断，len_a, len_b
        while len_a > len_b:
            len_a -= 1
            headA = headA.next
        while len_b > len_a:
            len_b -= 1
            headB = headB.next

        # 找到一样长的地方有没有相同的点
        # 这里注意不能用while headA.val !== headB.val
        # 因为有可能两个链表没有重合的部分，headA和headB都会为None，这样就没有val属性，所以会报错。
        while headA is not headB:
            headA = headA.next
            headB = headB.next

        return headA
