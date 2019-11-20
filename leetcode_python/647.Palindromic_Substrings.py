#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        #        a b c
        #      a 1 0 0
        #      b 0 1 0
        #      c 0 0 1

        #        a a a
        #     a  1 1 1
        #     a  0 1 1
        #     a  0 0 1

        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):  # axa, 如果长度为3，两边一样的话，中间无论什么都会是对称的
                    dp[i][j] = True
                    res += 1
        # print(dp)
        return res
