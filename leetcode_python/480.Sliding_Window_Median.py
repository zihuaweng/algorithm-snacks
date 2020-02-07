#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/sliding-window-median/

import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        heap = nums[:k]
        heap.sort()
        mid = k // 2
        if k % 2 == 0:
            res = [(heap[mid] + heap[mid - 1]) / 2]
        else:
            res = [heap[mid]]

        for i, n in enumerate(nums[k:]):
            # print(heap)
            idx = bisect.bisect(heap, nums[i])
            # print(idx)
            heap[idx - 1] = n
            heap.sort()
            if k % 2 == 0:
                res.append((heap[mid] + heap[mid - 1]) / 2)
            else:
                res.append(heap[mid])

        return res
