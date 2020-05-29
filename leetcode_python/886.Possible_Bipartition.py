#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        seen = [0] * (N + 1)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for n in range(1, N + 1):
            if seen[n] == 0:
                queue = [n]
                value = 1
                while queue:
                    temp = []
                    for k in queue:
                        if seen[k] != 0:
                            if seen[k] != value:
                                return False
                        else:
                            seen[k] = value
                            temp.extend(graph[k])
                    value *= -1
                    queue = temp
        return True


