# Maximum number of moves in a grid

[Problem link](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
 public:
  int maxMoves(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> dp(m);
    for (int j = n - 2; j >= 0; --j) {
      vector<int> cur(m);
      for (int i = 0; i < m; ++i)
        for (int ii = max(i - 1, 0); ii <= min(i + 1, m - 1); ++ii)
          if (grid[i][j] < grid[ii][j + 1]) cur[i] = max(cur[i], 1 + dp[ii]);
      dp = cur;
    }
    return *max_element(dp.begin(), dp.end());
  }
};
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Grid](/Collections/dynamic-programming.md#grid)
