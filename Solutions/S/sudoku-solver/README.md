# Sudoku solver

[Problem link](https://leetcode.com/problems/sudoku-solver)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sudoku-solver

class Solution {
 public:
  bool solveSudoku(vector<vector<char>>& board, int i = 0, int j = 0) {
    if (i == 9) return true;

    int ii = i, jj = j + 1;
    if (jj == 9) jj = 0, ++ii;

    if (board[i][j] != '.') return solveSudoku(board, ii, jj);
    vector<char> allow(9, 1);

    for (int x = 0; x < 9; ++x)
      if (board[x][j] != '.') allow[board[x][j] - '1'] = 0;
    for (int x = 0; x < 9; ++x)
      if (board[i][x] != '.') allow[board[i][x] - '1'] = 0;
    {
      int bi = i / 3, bj = j / 3;
      for (int x = 3 * bi; x < 3 * (bi + 1); ++x)
        for (int y = 3 * bj; y < 3 * (bj + 1); ++y)
          if (board[x][y] != '.') allow[board[x][y] - '1'] = 0;
    }

    for (char c = '1'; c <= '9'; ++c) {
      if (!allow[c - '1']) continue;
      board[i][j] = c;
      if (solveSudoku(board, ii, jj)) return true;
    }
    board[i][j] = '.';
    return false;
  }
};
```
### Solution.py
```py
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
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking) > [Minimum option optimisation](/Collections/backtracking.md#minimum-option-optimisation)
