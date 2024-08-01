# Toeplitz matrix

[Problem link](https://leetcode.com/problems/toeplitz-matrix/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/toeplitz-matrix/

class Solution {
 public:
  bool isToeplitzMatrix(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    for (int i = 1; i < m; ++i)
      for (int j = 1; j < n; ++j)
        if (matrix[i][j] != matrix[i - 1][j - 1]) return false;
    return true;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
