#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-median-from-data-stream/


class MedianFinder:

    # large_heap   [6,7,8]
    # small_heap   [4,2,1]

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []  # the larger half of the list, min heap
        self.small = []  # the smaller half of the list, max heap (invert min-heap)

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self) -> float:
        # print(self.large)
        # print(self.small)
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()