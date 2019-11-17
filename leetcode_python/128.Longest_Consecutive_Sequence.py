#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_len = 1
        temp = 1
        for i in range(1, len(nums)):
            # print(nums[i])
            if nums[i - 1] != nums[i]:
                if nums[i - 1] == nums[i] - 1:
                    temp += 1
                else:
                    max_len = max(max_len, temp)
                    temp = 1
        max_len = max(max_len, temp)
        return max_len


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        nums = set(nums)
        for n in nums:
            temp_res = 1
            if n - 1 not in nums:
                m = n
                while m + 1 in nums:
                    m += 1
                    temp_res += 1
                res = max(temp_res, res)
            # print(n, res)
        return res