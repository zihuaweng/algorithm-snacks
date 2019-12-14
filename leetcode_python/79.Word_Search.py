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



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #         [
        #           ['A','B','C','E'],
        #           ['S','F','C','S'],
        #           ['A','D','E','E']
        #         ]

        #         visited =  [
        #           [False,'B','C','E'],
        #           ['S','F','C','S'],
        #           ['A','D','E','E']
        #         ]
        self.direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, visited, word, i, j):
                    return True
        return False

    def dfs(self, board, visited, word, i, j):
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if visited[i][j] or board[i][j] != word[0]:
            return False

        visited[i][j] = True

        for x, y in self.direction:
            if self.dfs(board, visited, word[1:], i + x, j + y):
                return True

        visited[i][j] = False
        return False

