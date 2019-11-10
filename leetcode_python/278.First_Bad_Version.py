#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n - 1
        while i <= j:
            mid = (i + j) // 2   # 这里的Java实现会integer overflow， 所以最好i + (j-i) // 2
            if not isBadVersion(mid):
                i = mid + 1
            else:
                j = mid - 1

        return i