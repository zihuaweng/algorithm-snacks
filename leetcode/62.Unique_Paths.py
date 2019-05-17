# https://leetcode.com/problems/unique-paths/
# 典型动态规划问题，现保存一个二维列表，然后每一次结果是左边和上边的加和

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        paths = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    paths[i][j] = 1
                else:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[m - 1][n - 1]
