# https://leetcode.com/problems/add-two-numbers/
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        res = head
        carry = 0
        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            val = l1_val + l2_val + carry
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            a, b = divmod(val, 10)
            carry = a
            res.next = ListNode(b)
            res = res.next

        if carry > 0:
            res.next = ListNode(carry)

        return head.next


