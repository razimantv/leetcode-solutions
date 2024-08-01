# Difference between ones and zeros in row and column

[Problem link](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution {
 public:
  vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> row1(m), col1(n);
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        row1[i] += grid[i][j];
        col1[j] += grid[i][j];
      }

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) grid[i][j] = 2 * (row1[i] + col1[j]) - m - n;
    return grid;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Matrix](/Collections/matrix.md#matrix)
