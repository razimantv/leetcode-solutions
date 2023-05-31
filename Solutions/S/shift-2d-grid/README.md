# Shift 2d grid

[Problem link](https://leetcode.com/problems/shift-2d-grid)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shift-2d-grid

class Solution {
 public:
  vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
    int m = grid.size(), n = grid[0].size();
    auto grid2 = grid;
    k = k % (m * n);
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        int x = (i * n + j + m * n - k) % (m * n);
        grid[i][j] = grid2[x / n][x % n];
      }
    return grid;
  }
};
```