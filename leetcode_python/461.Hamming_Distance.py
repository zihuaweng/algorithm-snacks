#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/hamming-distance/
# 首先异或，求出不同的数字位数，然后计算1的个数

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = x^y
        c = 0
        while dis:
            dis &= (dis - 1)
            c+=1
        return c