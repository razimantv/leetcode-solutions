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