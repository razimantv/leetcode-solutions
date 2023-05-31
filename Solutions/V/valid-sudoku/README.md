# Valid sudoku

[Problem link](https://leetcode.com/problems/valid-sudoku)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-sudoku

class Solution {
 public:
  bool isValidSudoku(vector<vector<char>>& board) {
    vector<int> seen(10);
    int next = 1;

    for (int i = 0; i < 9; ++i) {
      for (int j = 0; j < 9; ++j) {
        if (board[i][j] == '.') continue;
        int c = board[i][j] - '0';
        if (seen[c] == next)
          return false;
        else
          seen[c] = next;
      }
      ++next;

      for (int j = 0; j < 9; ++j) {
        if (board[j][i] == '.') continue;
        int c = board[j][i] - '0';
        if (seen[c] == next)
          return false;
        else
          seen[c] = next;
      }
      ++next;

      int bi = i / 3, bj = i % 3;
      for (int x = 0; x < 3; ++x)
        for (int y = 0; y < 3; ++y) {
          int ii = bi * 3 + x, jj = bj * 3 + y;

          if (board[ii][jj] == '.') continue;
          int c = board[ii][jj] - '0';
          if (seen[c] == next)
            return false;
          else
            seen[c] = next;
        }
      ++next;
    }
    return true;
  }
};
```