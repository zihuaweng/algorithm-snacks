#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# similar questions
# https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)