#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5
# 比较难，需要递归dfs完成。

# Time complexity: O(k*2^n)
# Space complexity: O()


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k:
            return False
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)  # 倒排更快
        set_sum = [0] * k
        average_sum = sum(nums) // k

        def dfs(index):
            if index == len(nums):
                return True
            for i in range(k):
                set_sum[i] += nums[index]
                if set_sum[i] <= average_sum and dfs(index + 1):
                    return True
                set_sum[i] -= nums[index]
                if set_sum[i] == 0:  # 如果这个数不符合条件就没必要尝试别的空篮子，速度提高很多
                    break
            return False

        return dfs(0)