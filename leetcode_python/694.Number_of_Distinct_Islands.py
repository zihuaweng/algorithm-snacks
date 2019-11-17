#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        # 11011
        # 10000
        # 00001
        # 11011

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        res = set()

        def dfs(position, pos, i, j):
            x = i + pos[0]
            y = j + pos[1]
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = -1
            position.append(pos)
            for k in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                dfs(position, (pos[0] + k[0], pos[1] + k[1]), i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    positions = []
                    dfs(positions, (0, 0), i, j)
                    res.add(tuple(positions))
        # print(res)
        return len(res)

