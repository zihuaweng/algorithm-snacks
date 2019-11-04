#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(nm)
# Space complexity: O(n+m)


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        dis = [[] for _ in range(2001)]
        for i in range(n):
            for j in range(m):
                idx = self.dist(workers[i], bikes[j])
                dis[idx].append([i, j])

        assigned = [False for _ in range(n)]
        occupied = [False for _ in range(m)]
        res = [None] * n
        for d in dis:
            if d:
                for w, b in d:
                    if not assigned[w] and not occupied[b]:
                        res[w] = b
                        assigned[w] = True
                        occupied[b] = True

        return res

    def dist(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])