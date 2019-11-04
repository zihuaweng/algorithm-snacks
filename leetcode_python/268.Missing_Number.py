#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            res = res ^ i ^ nums[i]

        return res ^ n