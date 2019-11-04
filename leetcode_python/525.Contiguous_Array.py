#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/contiguous-array/

# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length = 0
        if not nums:
            return length

        _sum = 0
        count = {0: 0}
        for i, num in enumerate(nums, 1):
            if num == 0:
                _sum -= 1
            if num == 1:
                _sum += 1
            if _sum in count:
                length = max(length, i - count[_sum])
            else:
                count[_sum] = i

        return length