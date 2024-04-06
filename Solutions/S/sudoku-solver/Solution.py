# https://leetcode.com/problems/sudoku-solver

class Solution:
    def update_constraints(self, board, constraints, i, j, val, delta):
        for ii in range(9):
            if board[ii][j] == '.':
                constraints[ii][j][val] += delta
        for jj in range(9):
            if board[i][jj] == '.':
                constraints[i][jj][val] += delta
        bi, bj = i // 3, j // 3
        for di in range(3):
            for dj in range(3):
                ii, jj = bi * 3 + di, bj * 3 + dj
                if board[ii][jj] == '.':
                    constraints[ii][jj][val] += delta

    def backtrack(self, board, constraints):
        inext, jnext, best = -1, -1, [-1] * 10
        for i, row in enumerate(board):
            for j, dig in enumerate(row):
                if dig == '.':
                    cur = [d for d in range(9) if not constraints[i][j][d]]
                    if not cur:
                        return False
                    elif len(cur) < len(best):
                        inext, jnext, best = i, j, cur

        if inext == -1:
            return True

        for d in best:
            board[inext][jnext] = str(d + 1)
            self.update_constraints(board, constraints, inext, jnext, d, 1)
            if self.backtrack(board, constraints):
                return True
            self.update_constraints(board, constraints, inext, jnext, d, -1)

        board[inext][jnext] = '.'
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        constraints = [[[0 for d in range(9)]
                        for j in range(9)] for i in range(9)]

        for i, row in enumerate(board):
            for j, dig in enumerate(row):
                if dig == '.':
                    continue
                val = int(dig) - 1
                self.update_constraints(board, constraints, i, j, val, 1)

        self.backtrack(board, constraints)
