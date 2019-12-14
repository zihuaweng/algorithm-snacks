#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 1231. Divide Chocolate
# Capacity To Ship Packages In N Days
# Koko Eating Bananas
# Minimize Max Distance to Gas Station
# Split Array Largest Sum


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def valid(mid):
            c = sum((p + mid - 1) // mid for p in piles)
            return True if c > H else False

        i = 1
        j = max(piles)
        while i <= j:
            mid = (i + j) // 2
            if valid(mid):
                i = mid + 1
            else:
                j = mid - 1

        return i