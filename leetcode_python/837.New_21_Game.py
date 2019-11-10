#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/new-21-game/

# Time complexity: O(m)
# Space complexity: O()

# https://leetcode.com/problems/new-21-game/discuss/132503/My-take-on-how-to-reach-at-Solution

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N > K - 1 + W or K == 0:
            return 1

        dp = [0 for _ in range(N + 1)]
        dp[0] = 1
        prop = 1 / W
        prev = 0

        # for less than K
        for i in range(1, K + 1):
            start = dp[i - W - 1] if i - W - 1 >= 0 else 0
            prev = prev - start + dp[i - 1]
            dp[i] = prev * prop

        # for more than K
        res = dp[K]
        for i in range(K + 1, N + 1):
            start = dp[i - W - 1] if i - W - 1 >= 0 else 0
            prev = prev - start
            dp[i] = prev * prop
            res += dp[i]

        return res
