#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n^2)
# Space complexity: O(n^2)

# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        #    b   b   b   a   b
        # b  1   2   3   3   4
        # b      1   2   2   3
        # b      0   1   1   3
        # a              1   1
        # b                  1
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
