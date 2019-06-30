#  https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 设置两个指针，头指针先往前面移动n个位置，然后头，尾指针同时往前移动直至最后

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        slow = res
        fast = res
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return res.next
