# Number of submatrices that sum to target

[Problem link](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target

class Solution {
 public:
  int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size(), ret = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j)
        matrix[i][j] += (j ? matrix[i][j - 1] : 0) +
                        (i ? matrix[i - 1][j] : 0) -
                        ((i * j) ? matrix[i - 1][j - 1] : 0);
      for (int ii = 0; ii <= i; ++ii) {
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        for (int j = 0; j < n; ++j) {
          int psum = matrix[i][j] - (ii ? matrix[ii - 1][j] : 0);
          ret += cnt[psum - target];
          ++cnt[psum];
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
* [Matrix](/Collections/matrix.md#matrix) > [Row pair processing](/Collections/matrix.md#row-pair-processing)
