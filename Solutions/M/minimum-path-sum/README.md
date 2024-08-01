# Minimum path sum

[Problem link](https://leetcode.com/problems/minimum-path-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-path-sum

class Solution {
 public:
  int minPathSum(vector<vector<int>>& grid) {
    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid[i].size(); j++) {
        if (i == 0 and j == 0) continue;
        if (i == 0)
          grid[i][j] += grid[i][j - 1];
        else if (j == 0)
          grid[i][j] += grid[i - 1][j];
        else
          grid[i][j] += min(grid[i][j - 1], grid[i - 1][j]);
      }
    }

    return grid.back().back();
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
