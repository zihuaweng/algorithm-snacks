# https://leetcode.com/problems/number-of-islands/
# 遍历矩阵，只要遇到“1”就执行helper
# helper里面是每次遇到“1”，就标记成走过了，知道没有“1”为止，这样算是一个小岛

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.helper(row, col, grid)
        return count

    def helper(self, row, col, grid):
        if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
            return
        if grid[row][col] != "1":
            return
        # 已经走过的地方替换成2
        grid[row][col] = "2"
        self.helper(row + 1, col, grid)
        self.helper(row - 1, col, grid)
        self.helper(row, col - 1, grid)
        self.helper(row, col + 1, grid)
