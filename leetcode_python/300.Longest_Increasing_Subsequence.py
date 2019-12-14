#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf

# dp 解答：
# n^2
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        # print(dp)
        return max(dp)

# 一只生成新的数组，每次新数用二分搜索查找可以插入的位置，如果是==length就+1
# 否则就覆盖原来的数据
# nlogn
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        length = 0
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            # print(dp, idx)
            if idx == length:
                length += 1
                dp.append(num)
            else:
                dp[idx] = num

        return length



