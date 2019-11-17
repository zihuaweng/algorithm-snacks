#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        counter[0] = -1
        pre_sum = 0
        min_len = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            target = pre_sum - k
            if target in counter:
                min_len = max(min_len, i - counter[target])
            if pre_sum not in counter:
                counter[pre_sum] = i
        return min_len
