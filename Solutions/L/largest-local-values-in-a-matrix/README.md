# Largest local values in a matrix

[Problem link](https://leetcode.com/problems/largest-local-values-in-a-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution {
 public:
  vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> ret(n - 2, vector<int>(n - 2, INT_MIN));
    for (int i = 0; i < n - 2; ++i)
      for (int j = 0; j < n - 2; j++)
        for (int k = i; k < i + 3; ++k)
          for (int l = j; l < j + 3; ++l)
            ret[i][j] = max(ret[i][j], grid[k][l]);
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
