# Rotting oranges

[Problem link](https://leetcode.com/problems/rotting-oranges)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rotting-oranges

class Solution {
 public:
  int orangesRotting(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid[0].size();
    for (int t = 0; t < m * n + 1; ++t) {
      bool f1 = false, f2 = false;
      for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
          if (grid[i][j] != 1) continue;
          f1 = true;
          if ((i > 0 and grid[i - 1][j] == 2) or
              (i + 1 < m and grid[i + 1][j] == 2) or
              (j > 0 and grid[i][j - 1] == 2) or
              (j + 1 < n and grid[i][j + 1] == 2)) {
            grid[i][j] = 3;
            f2 = true;
          }
        }
      }
      if (!f1) return t;
      if (!f2) return -1;

      for (auto &r : grid)
        for (int &v : r)
          if (v == 3) v = 2;
    }
    return -1;
  }
};
```