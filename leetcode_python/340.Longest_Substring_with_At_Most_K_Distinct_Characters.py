#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0
        i = 0
        j = 0
        counter = {}
        max_len = 0
        while j < len(s):
            while j < len(s) and len(counter) <= k:
                char = s[j]
                if char in counter:
                    counter[char] += 1
                else:
                    if len(counter) == k:
                        break
                    else:
                        counter[char] = 1
                j += 1

            max_len = max(max_len, j - i)

            while len(counter) == k:
                char = s[i]
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
                i += 1

        return max_len


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        ans = 0
        l = 0
        for r, c in enumerate(s):
            d[c] = r
            if len(d) > k:
                l = min(d.values())
                del d[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans


