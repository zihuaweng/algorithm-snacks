#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        slow = 0
        fast = 0
        counter = {}
        max_len = 0
        while fast < len(s):
            while fast < len(s) and len(counter) <= k:
                char = s[fast]
                if char in counter:
                    counter[char] += 1
                else:
                    if len(counter) == k:
                        break
                    else:
                        counter[char] = 1
                fast += 1

            max_len = max(max_len, fast - slow)

            while len(counter) == k:
                char = s[slow]
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
                slow += 1

        return max_len

