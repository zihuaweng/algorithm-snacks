#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 4  # 每个格子都是4-相邻的边
                    if i > 0 and grid[i - 1][j] == 1: count -= 1
                    if i < m - 1 and grid[i + 1][j] == 1: count -= 1
                    if j > 0 and grid[i][j - 1] == 1: count -= 1
                    if j < n - 1 and grid[i][j + 1] == 1: count -= 1
        return count



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i < m - 1 and grid[i + 1][j] == 1: res -= 2
                    if j < n - 1 and grid[i][j + 1] == 1: res -= 2
        return res
