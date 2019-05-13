#  https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 设置两个指针，头指针先往前面移动n个位置，然后头，尾指针同时往前移动直至最后

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        end_i = 0
        end = head
        while end.next is not None and end_i < n - 1:
            end = end.next
            end_i += 1

        start = head
        res = []
        while end.next is not None:
            res.append(start.val)
            start = start.next
            end = end.next

        start = start.next

        while start and start.next is not None:
            res.append(start.val)
            start = start.next

        if start:
            res.append(start.val)

        return res
