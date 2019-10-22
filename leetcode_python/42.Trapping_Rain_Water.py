#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/trapping-rain-water/solution/

# 动态规划
# youtube.com/watch?v=wz00uI9mDXA
# 每个槽需要知道左边最高和右边最高，能承载的水量是当前的min(right_highest, left_highest[i]) - height[i]。
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ans = 0

        left_highest = [0] * len(height)
        for i in range(1, len(left_highest)):
            left_highest[i] = max(left_highest[i - 1], height[i - 1])

        right_highest = 0
        for i in range(len(height) - 1, -1, -1):
            temp = min(right_highest, left_highest[i]) - height[i]
            if temp > 0:
                ans += temp
            right_highest = max(right_highest, height[i])

        return ans


# 双指针方法
# https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.
