#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/is-graph-bipartite/
# 能不能分成两部分要看第一部分与第二部分有没有相连的线
# 首先第一部分标记成0， 与之相连的都是1，如果再次碰到1，发现应该标记成0的话，证明之间有相关，不能分成两部分。

# Time complexity: O(n+k)
# Space complexity: O(n)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(node):
            for i in graph[node]:
                if i in color:
                    if color[node] == color[i]:
                        return False
                else:
                    color[i] = 1 - color[node]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True