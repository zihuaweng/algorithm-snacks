#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        slow = fast = 0
        count = 0
        max_len = 0

        while fast < n:
            if A[fast] == 0:
                count += 1
            fast += 1

            while count > K:
                if A[slow] == 0:
                    count -= 1
                slow += 1

            max_len = max(max_len, fast - slow)

        return max_len

