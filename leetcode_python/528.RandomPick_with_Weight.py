#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    # 1 8  9  3  6
    # 1 9 18  21  27
    # 20

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.s = w[-1]
        self.w = w

    def pickIndex(self) -> int:
        seed = random.randint(1, self.s)
        l = 0
        r = len(self.w) - 1
        while l < r:   # 注意边界
            mid = (l + r) // 2
            if self.w[mid] < seed:
                l = mid + 1  # 注意边界
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()