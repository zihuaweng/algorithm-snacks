#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/move-zeroes/
# 两个指针方法

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while nums[p2] != 0:
            p1 += 1
            p2 += 1
            if p2 == len(nums):
                return nums

        p2 += 1

        while p2 < len(nums):
            if nums[p2] != 0:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p1 += 1
            p2 += 1

        return nums