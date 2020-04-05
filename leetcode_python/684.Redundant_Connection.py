#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/redundant-connection/
# union find

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges))]

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x == p_y:
                return False
            parent[p_y] = p_x
            return True

        for i, j in edges:
            if not union(i - 1, j - 1):
                return [i, j]
