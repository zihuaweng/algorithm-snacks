#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/merge-k-sorted-lists/
# 遇到排序问题用priorityqueue或者heap
# 分别是：
# from Queue import PriorityQueue
# import heapq


# Time complexity: O(nlong(k))
# Space complexity: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not any(lists):
            return None

        n = len(lists)
        heap = []
        ans = ListNode(0)
        tail = ans
        for i in range(n):   # 首先构建一个heap
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:   # 遍历所有node然后加入heap
            val, index = heapq.heappop(heap)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next

        return ans.next


