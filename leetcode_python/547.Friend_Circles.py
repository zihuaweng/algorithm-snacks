#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/friend-circles/
# 这个题目是需要将方阵的长度个人分成不同群体，可以使用dfs

# Time complexity: O(N+K)
# Space complexity: O(N)


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()

        def dfs(node):
            for i, j in enumerate(M[node]):
                if j == 1 and i not in seen:
                    seen.add(i)
                    dfs(i)

        res = 0
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                res += 1

        return res

    # dfs另一种写法
    def findCircleNum2(self, M: List[List[int]]) -> int:
        seen = set()
        res = 0
        for i in range(len(M)):
            if i not in seen:
                to_see = [i]
                while to_see:
                    cur = to_see.pop()
                    if cur not in seen:
                        seen.add(cur)
                        for j, k in enumerate(M[cur]):
                            if k == 1 and j not in seen:
                                to_see.append(j)
                res += 1

        return res