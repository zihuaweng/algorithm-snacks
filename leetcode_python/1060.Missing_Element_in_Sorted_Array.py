#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# # https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i + j + 1) // 2
            if nums[mid] - nums[0] - mid >= k:
                j = mid - 1
            else:
                i = mid

        return k + nums[0] + i