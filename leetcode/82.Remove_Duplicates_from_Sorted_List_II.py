# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        temp = ListNode(0)
        temp.next = head
        pre = temp
        cur = head

        while cur is not None:
            while cur.next is not None and cur.next.val == cur.val:
                cur = cur.next
            if pre.next is cur:
                pre = pre.next
            else:
                pre.next = cur.next

            cur = cur.next

        return temp.next
