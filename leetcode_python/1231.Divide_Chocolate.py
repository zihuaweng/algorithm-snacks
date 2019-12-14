#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/divide-chocolate/

class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:

        def valid(mid):
            count = 1
            total = 0
            for s in sweetness:
                total += s
                if total > mid:
                    total = 0  # 这里和410不一样，本题目是想得到最低的值，所以超过了mid没关系，410需要所有都在mid里面。
                    count += 1
                    if count > K + 1:
                        return False
            return True

        i = min(sweetness)
        j = sum(sweetness) // (K + 1)
        while i <= j:
            mid = (i + j) // 2
            if valid(mid):
                j = mid - 1
            else:
                i = mid + 1

        return i

