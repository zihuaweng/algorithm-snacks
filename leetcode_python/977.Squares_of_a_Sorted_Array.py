#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x*x, A))