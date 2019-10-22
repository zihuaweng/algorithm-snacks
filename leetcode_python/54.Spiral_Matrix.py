#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(mn)
# Space complexity: O()

# 简单方法，速度慢
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


# 更快的方法
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        res = []
        while up < down and left < right:
            res.extend([matrix[up][i] for i in range(left, right)])
            res.extend([matrix[i][right] for i in range(up, down)])
            res.extend([matrix[down][i] for i in range(right, left, -1)])
            res.extend([matrix[i][left] for i in range(down, up, -1)])
            up += 1
            down -= 1
            left += 1
            right -= 1
        if left == right:
            res.extend([matrix[i][left] for i in range(up, down+1)])
        elif up == down:
            res.extend([matrix[up][i] for i in range(left, right + 1)])

        return res