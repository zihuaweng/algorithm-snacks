# https://leetcode.com/problems/rotate-image/
# 这道题直接循环做会很繁琐
# 可以选择对角线互换，互换后再翻转列表。
# 互换的小技巧是左上角互换写起来更容易，这样后面翻转列表需要一个循环。


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
