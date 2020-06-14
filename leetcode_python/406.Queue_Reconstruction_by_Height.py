#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(nlogn)
# Space complexity: O(n)


# https://leetcode.com/problems/queue-reconstruction-by-height/
# 先放入小的，然后放入大的

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        l = len(people)
        res = [None] * l
        people.sort()
        for cur in people:
            height, num = cur
            i = 0
            while i < l and num >= 0:
                if not res[i]:
                    if num == 0:
                        res[i] = cur
                    num -= 1
                else:
                    if res[i][0] == height:
                        num -= 1
                i += 1
        return res

# 先放入大的，然后放入小的
# 使用insert 速度更快
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for cur in people:
            res.insert(cur[1], cur)
        return res

