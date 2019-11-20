#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# # https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0

        diff = nums[-1] - nums[0] + 1
        missing = diff - len(nums)
        if k > missing:
            return nums[-1] + k - missing

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing
            else:
                right = mid

        return nums[left] + k
