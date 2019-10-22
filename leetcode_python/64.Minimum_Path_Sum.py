# https://leetcode.com/problems/minimum-path-sum/
# 典型递归计算
# 一开始先把第一行和第一列给填完是比较快的方式
# 如果每层去判断是不是小于零有点浪费时间

class Solution:
    def minPathSum(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for row in range(1, rows):
            grid[row][0] += grid[row - 1][0]
        for col in range(1, cols):
            grid[0][col] += grid[0][col - 1]
        for row in range(1, rows):
            for col in range(1, cols):
                left = grid[row][col - 1] + grid[row][col]
                up = grid[row - 1][col] + grid[row][col]
                grid[row][col] = min(left, up)

        return grid[rows - 1][cols - 1]
