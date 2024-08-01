# Minimum falling path sum

[Problem link](https://leetcode.com/problems/minimum-falling-path-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
 public:
  int minFallingPathSum(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    for (int i = 1; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        int best = INT_MAX;
        for (int k = max(0, j - 1); k < min(n, j + 2); ++k)
          best = min(best, matrix[i - 1][k]);
        matrix[i][j] += best;
      }
    return *min_element(matrix.back().begin(), matrix.back().end());
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
