# https://leetcode.com/problems/number-of-islands/
# 遍历矩阵，只要遇到“1”就执行helper
# helper里面是每次遇到“1”，就标记成走过了，知道没有“1”为止，这样算是一个小岛

# Time complexity:  O(N*M)
# Space complexity:  O(1)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.helper(i, j, grid)
        return count

    def helper(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            return

        grid[x][y] = '2'
        for _x, _y in self.d:
            self.helper(x + _x, y + _y, grid)


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