#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        # [2, 3, 1,  2, 4,  3]
        #  i
        #            j
        if not nums:
            return 0
        i = 0
        j = 0
        total_sum = 0
        min_len = len(nums) + 1
        while j < len(nums):
            total_sum += nums[j]

            while total_sum >= s:
                min_len = min(min_len, j - i + 1)
                total_sum -= nums[i]
                i += 1

            j += 1

        if min_len <= len(nums):
            return min_len
        else:
            return 0
