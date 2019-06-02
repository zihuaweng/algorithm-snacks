# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        header = ListNode(0)
        rest = head

        while rest is not None:
            temp = header.next
            header.next = rest
            rest = rest.next
            header.next.next = temp

        return header.next
