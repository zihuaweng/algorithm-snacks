# https://leetcode.com/problems/n-queens/ 

# 这道题，两个Queen不能同时放在同一行，同一列，或者对角线上
# 对角线一共有2*n-1条，我们保存到left_corner和right_corner
# queue每次走一行，然后记录当前这一行的Queen应该放在哪一col

# 另一种解法： https://www.youtube.com/watch?v=Xa-yETqFNEQ

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, left_corner, right_corner):
            row = len(queens)
            if row == n:
                res.append(queens)
                return
            
            for col in range(n):
                left = row+col   # 45度对角线
                right = row-col+n-1   # 135度对角线
                if col not in queens and left not in left_corner and right not in right_corner:
                    dfs(queens+[col], left_corner+[left], right_corner+[right])
                    
        res = []
        dfs([], [], [])
        result = []
        for r in res:
            queen = []
            for col in r:
                queen.append('.'*col + 'Q' + '.'*(n-col-1))
            result.append(queen)
        return result