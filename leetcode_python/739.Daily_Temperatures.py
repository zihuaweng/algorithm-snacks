#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# stack

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
