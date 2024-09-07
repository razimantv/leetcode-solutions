# Range sum query 2d immutable

[Problem link](https://leetcode.com/problems/range-sum-query-2d-immutable)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix {
 public:
  vector<vector<long long>> psum;
  NumMatrix(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    psum = vector<vector<long long>>(m + 1, vector<long long>(n + 1));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        psum[i + 1][j + 1] =
            psum[i][j + 1] + psum[i + 1][j] - psum[i][j] + matrix[i][j];
  }

  int sumRegion(int row1, int col1, int row2, int col2) {
    return psum[row2 + 1][col2 + 1] - psum[row1][col2 + 1] -
           psum[row2 + 1][col1] + psum[row1][col1];
  }
};

```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
