# https://leetcode.com/problems/number-of-islands/
# 遍历矩阵，只要遇到“1”就执行helper
# helper里面是每次遇到“1”，就标记成走过了，知道没有“1”为止，这样算是一个小岛

# Time complexity:  O(N*M)
# Space complexity:  O(1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.count_island(grid, i, j)
        return count

    def count_island(self, grid, i, j):
        if grid[i][j] != '1':
            return
        grid[i][j] = '2'
        for _x, _y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x = i + _x
            new_y = j + _y
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                self.count_island(grid, new_x, new_y)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        res = 0
        m = len(grid)
        n = len(grid[0])
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            stack = [(x, y)]
            for point in stack:
                for _x, _y in direction:
                    new_x = point[0] + _x
                    new_y = point[1] + _y
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = '2'    # 加进去之前就要判断，不然需要很多重复计算
                        stack.append((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '2'
                    res += 1
                    dfs(i, j)

        return res