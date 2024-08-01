# Check if matrix is x matrix

[Problem link](https://leetcode.com/problems/check-if-matrix-is-x-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-matrix-is-x-matrix

class Solution {
 public:
  bool checkXMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        if (i == j or i + j == n - 1) {
          if (!grid[i][j]) return false;
        } else if (grid[i][j])
          return false;
      }
    return true;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
