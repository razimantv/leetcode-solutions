# Game of life

[Problem link](https://leetcode.com/problems/game-of-life)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/game-of-life

class Solution {
 public:
  void gameOfLife(vector<vector<int>>& board) {
    auto ret{board};
    int neigh[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1},
                       {0, 1},   {1, -1}, {1, 0},  {1, 1}};
    for (int m = board.size(), n = board[0].size(), i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int cnt = 0;
        for (int k = 0; k < 8; ++k) {
          int ii = i + neigh[k][0], jj = j + neigh[k][1];
          if (ii >= 0 and ii < m and jj >= 0 and jj < n) cnt += board[ii][jj];
        }
        ret[i][j] = (cnt == 3 or (cnt == 2 and board[i][j]));
      }
    }
    board = ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
