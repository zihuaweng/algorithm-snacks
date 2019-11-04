#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/string-transforms-into-another-string/


# Time complexity: O(n)
# Space complexity: O()

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        n = len(str1)
        change = {}
        for i in range(n):
            if str1[i] not in change:
                change[str1[i]] = str2[i]
            elif change[str1[i]] != str2[i]:
                return False

        return len(set(str2)) < 26

