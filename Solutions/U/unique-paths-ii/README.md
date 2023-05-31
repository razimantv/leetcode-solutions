# Unique paths ii

[Problem link](https://leetcode.com/problems/unique-paths-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-paths-ii

class Solution {
 public:
  int uniquePathsWithObstacles(vector<vector<int>>& grid) {
    int M = grid.size(), N = grid[0].size();
    if (grid[0][0] or grid[M - 1][N - 1]) return 0;

    grid[0][0] = 1;
    for (int j = 1; j < N; ++j) grid[0][j] = (1 - grid[0][j]) * grid[0][j - 1];
    for (int i = 1; i < M; ++i) {
      grid[i][0] = (1 - grid[i][0]) * grid[i - 1][0];
      for (int j = 1; j < N; ++j) {
        if (grid[i][j] == 1)
          grid[i][j] = 0;
        else
          grid[i][j] = grid[i - 1][j] + grid[i][j - 1];
      }
    }
    return grid.back().back();
  }
};
```