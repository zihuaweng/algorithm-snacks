#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/partition-equal-subset-sum/
# 同698，答案还需要琢磨

# Time complexity: O()
# Space complexity: O()


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        average_sum = sum(nums) // 2
        set_sum = [0, 0]

        nums.sort(reverse=True)

        def dfs(index):
            if index == len(nums):
                return True
            for i in range(2):
                set_sum[i] += nums[index]
                if set_sum[i] <= average_sum and dfs(index + 1):
                    return True
                set_sum[i] -= nums[index]
                if set_sum[i] == 0:
                    break
            return False

        return dfs(0)
