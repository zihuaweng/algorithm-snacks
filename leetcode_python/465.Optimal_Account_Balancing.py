#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/optimal-account-balancing/

# Time complexity: O()
# Space complexity: O()


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        total = collections.defaultdict(int)
        for send, receive, money in transactions:
            total[send] -= money
            total[receive] += money

        debt = [x for x in total.values() if x != 0]
        return self.dfs(0, 0, debt)

    def dfs(self, idx, trans, debt):
        while idx < len(debt) and debt[idx] == 0:
            idx += 1

        if idx >= len(debt):
            return trans

        min_trans = float('inf')
        for i in range(idx + 1, len(debt)):
            if debt[i] * debt[idx] < 0:
                debt[i] += debt[idx]
                temp_min_trans = self.dfs(idx + 1, trans + 1, debt)
                min_trans = min(min_trans, temp_min_trans)
                debt[i] -= debt[idx]

        return min_trans
