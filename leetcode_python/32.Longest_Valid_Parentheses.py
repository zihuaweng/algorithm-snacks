#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        #         )   (  (      (         )       )     (       )   ) )
        # idx    0   1   2     3         4       5     6        7
        # left   -1  0   0     0         0       0     0        0
        # stack  [] [1]  [1,2] [1,2,3]  [1,2]   [1]   [1,6]    [1]
        # max    0   0    0     0       4-2     5-1    4       7-1

        if not s:
            return 0

        left = -1
        stack = []
        max_len = 0
        for i in range(len(s)):
            if s[i] == ')':
                if stack:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - left)
                else:
                    left = i
            else:
                stack.append(i)

        return max_len




