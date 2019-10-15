#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 这道题的意思是说让找到所有点既可以走到左面，上面（pacific）又可以走到右面，下面（atlantic）
# dfs的思路就是，逆向思维，找到从左边,上面（就是第一列&第一排，已经是pacific的点）出发，能到的地方都记录下来.
# 同时右面，下面（就是最后一列，最后一排，已经是Atlantic的点）出发，能到的地方记录下来。
# 综合两个visited矩阵，两个True，证明反过来这个点可以到两个海洋。

# Time complexity: O(MN)
# Space complexity: O(MN)


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        pacific_m = [[False for _ in range(n)] for _ in range(m)]
        atlantic_m = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            # 从第一列（pacific）到对面atlantic
            self.dfs(matrix, i, 0, pacific_m)
            # 从最后一列（atlantic）到对面pacific
            self.dfs(matrix, i, n - 1, atlantic_m)

        for i in range(n):
            # 从第一行（pacific）到最后一行atlantic
            self.dfs(matrix, 0, i, pacific_m)
            # 从最后一行（atlantic）到第一行pacific
            self.dfs(matrix, m - 1, i, atlantic_m)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific_m[i][j] and atlantic_m[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, x, y, visited):
        visited[x][y] = True
        # 存放一个四个方位的var方便计算左右上下
        for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + i, y + j
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and not visited[nx][ny] and matrix[nx][ny] >= \
                    matrix[x][y]:
                self.dfs(matrix, nx, ny, visited)


# 第二种方法是bfs，使用一个queue去记录可以到达的点，最后同样是合并来给你个能到达的列表的重合返回。

class Solution2:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        # 存放一个四个方位的var方便计算左右上下
        self.direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        pacific_set = set([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        atlantic_set = set([(m - 1, i) for i in range(n)] + [(j, n - 1) for j in range(m)])

        def bfs(reachable_point):
            queue = collections.deque(reachable_point)
            while queue:
                x, y = queue.popleft()
                for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nx, ny = x + i, y + j
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and (nx, ny) not in reachable_point and \
                            matrix[nx][ny] >= matrix[x][y]:
                        reachable_point.add((nx, ny))
                        queue.append((nx, ny))
            return reachable_point

        return list(bfs(pacific_set) & bfs(atlantic_set))





