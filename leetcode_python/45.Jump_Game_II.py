#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# [2,3,1,1,4]
# [0,1,2,3,4]
# 开始 0
# 第一步 1,2 走到2为当前终点，需要走第二步
# 第二部 3,4，到4就到达终点了
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_end = 0
        step = 0
        for i, val in enumerate(nums[:-1]):
            max_end = max(max_end, i + val)
            if i == end:
                end = max_end
                step += 1
        return step

