# https://leetcode.com/problems/n-queens

class Solution:
    def backtrack(self, n, i, blocked, board, ret):
        if i == n:
            ret.append([''.join(row) for row in board])
            return
        
        for j in range(n):
            if blocked[i][j]: continue

            board[i][j] = 'Q'
            for k in range(1, n-i):
                blocked[i+k][j] += 1
                if j+k < n: blocked[i+k][j+k] += 1
                if j-k >= 0: blocked[i+k][j-k] += 1

            self.backtrack(n, i+1, blocked, board, ret)
            board[i][j] = '.'
            for k in range(1, n-i):
                blocked[i+k][j] -= 1
                if j+k < n: blocked[i+k][j+k] -= 1
                if j-k >= 0: blocked[i+k][j-k] -= 1
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        blocked = [[0 for i in range(n)] for j in range(n)]
        board = [['.' for i in range(n)] for j in range(n)]
        ret = []
        self.backtrack(n, 0, blocked, board, ret)
        return ret
