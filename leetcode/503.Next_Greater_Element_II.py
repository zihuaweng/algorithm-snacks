#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/next-greater-element-ii/
# https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice
# stack存入nums的index，如果遇到有比他大的，pop出来，res得到结果，如果没有比他大的，继续加入下一个index
# 第二个循环用来查看是不是已经走完了，stack没有东西的话就可以结束

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        # 第一个循环
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        # 第二个循环
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            if not stack:
                break
        return res
