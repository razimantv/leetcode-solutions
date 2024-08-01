# Maximum sum of an hourglass

[Problem link](https://leetcode.com/problems/maximum-sum-of-an-hourglass/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution {
 public:
  int maxSum(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int best = 0;
    for (int i = 1; i < m - 1; ++i) {
      for (int j = 1; j < n - 1; ++j) {
        int cur = grid[i][j];
        for (int k = j - 1; k <= j + 1; ++k)
          cur += grid[i - 1][k] + grid[i + 1][k];
        best = max(best, cur);
      }
    }
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
