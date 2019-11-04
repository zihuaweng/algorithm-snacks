#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def valid(mid):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low


# https://leetcode.com/problems/split-array-largest-sum/discuss/141497/AC-Java-DFS-%2B-memorization
# dp 做法
# https://leetcode.com/problems/split-array-largest-sum/discuss/89821/Python-solution-dp-and-binary-search