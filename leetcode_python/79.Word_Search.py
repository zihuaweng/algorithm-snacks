# https://leetcode.com/problems/word-search/
# dfs思想，注意到了边界需要判断
# 记录走过没有可以直接替换原始board，这样可以节省空间
# 每次走完一步要记得回溯过去

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == '':
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        # passed = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.helper(board, word, i, j):
                    return True

        return False

    def helper(self, board, word, row, col):
        if word == '':
            return True
        if col < 0 or col >= len(board[0]) or row < 0 or row >= len(board):
            return False
        if board[row][col] == '#' or board[row][col] != word[0]:
            return False

        temp = board[row][col]
        board[row][col] = '#'
        word = word[1:]

        if self.helper(board, word, row - 1, col) or self.helper(board, word, row + 1, col) or self.helper(board, word,
                                                                                                           row,
                                                                                                           col - 1) or self.helper(
                board, word, row, col + 1):
            return True
        # 要记得回溯
        board[row][col] = temp

