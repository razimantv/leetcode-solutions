# Transpose matrix

[Problem link](https://leetcode.com/problems/transpose-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/transpose-matrix

class Solution {
 public:
  vector<vector<int>> transpose(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    auto ret = vector<vector<int>>(n, vector<int>(m));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) ret[j][i] = matrix[i][j];
    return ret;
  }
};
```