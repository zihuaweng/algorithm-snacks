#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()

        def happy_sum(target):
            temp_sum = 0
            for i in str(target):
                temp_sum += int(i) ** 2

            if temp_sum == 1:
                return True
            elif temp_sum in sum_set:
                return False
            else:
                sum_set.add(temp_sum)
                return True if happy_sum(temp_sum) else False

        return happy_sum(n)