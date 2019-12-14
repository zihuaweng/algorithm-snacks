#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 410一样的代码

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def valid(mid):
            count = 1
            total = 0
            for w in weights:
                total += w
                if total > mid:
                    count += 1
                    total = w
                    if count > D:
                        return False
            return True

        i = max(weights)
        j = sum(weights)
        while i <= j:
            mid = (i + j) // 2
            if valid(mid):
                j = mid - 1
            else:
                i = mid + 1

        return i