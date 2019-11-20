#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_map:
                left = max(left, char_map[char] + 1)

            char_map[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len