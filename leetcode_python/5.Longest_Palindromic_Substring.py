#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #         a  b  a
        #         |(检查左右是否相等)
        #            |
        #               |

        #         a b b a
        #         |(检查左右是否相等)
        #           |
        #             |
        #               |
        res = ''
        for i in range(len(s)):
            #           检查奇数情况 aba,         检查偶数情况 abba
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

