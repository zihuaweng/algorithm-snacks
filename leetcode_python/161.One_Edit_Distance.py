#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if n < m:
            return self.isOneEditDistance(t, s)

        if n - m > 1:
            return False
        elif n == m:
            diff = 0
            for i in range(m):
                if s[i] != t[i]:
                    diff += 1
            return diff == 1
        else:
            i = 0
            while i < m:
                if s[i] != t[i]:
                    break
                i += 1
            for j in range(i, m):
                if s[j] != t[j + 1]:
                    return False
            return True
