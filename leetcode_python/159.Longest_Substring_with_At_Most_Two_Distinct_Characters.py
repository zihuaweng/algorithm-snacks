#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# 类似340. Longest Substring with At Most K Distinct Characters

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        ans = 0
        l = 0
        for r, c in enumerate(s):
            d[c] = r
            if len(d) > 2:
                l = min(d.values())
                del d[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
