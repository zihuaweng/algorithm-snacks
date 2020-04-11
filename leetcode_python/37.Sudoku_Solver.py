#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.check_list = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    self.check_list.append((row, col))
        self.solver(0)

    def solver(self, cur):
        if cur == len(self.check_list):
            return True
        row, col = self.check_list[cur]
        for num in range(1, 10):
            if self.valid(row, col, str(num)):
                self.board[row][col] = str(num)
                if self.solver(cur + 1):
                    return True
                self.board[row][col] = '.'
        return False

    def valid(self, row, col, new_str):
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(9):
            if self.board[i][col] == new_str:
                return False
            if self.board[row][i] == new_str:
                return False
            if self.board[start_row + i // 3][start_col + i % 3] == new_str:
                return False
        return True
