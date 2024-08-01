# Disconnect path in a binary matrix by at most one flip

[Problem link](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

class Solution {
 public:
  bool isPossibleToCutPath(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if ((i + j) and (!i or !grid[i - 1][j]) and (!j or !grid[i][j - 1]))
          grid[i][j] = 0;
    if (!grid[m - 1][n - 1]) return true;
    for (int i = m; i--;)
      for (int j = n; j--;)
        if ((i + j < m + n - 2) and (i == m - 1 or !grid[i + 1][j]) and
            (j == n - 1 or !grid[i][j + 1]))
          grid[i][j] = 0;

    vector<vector<int>> psum(m, vector<int>(n));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        psum[i][j] = grid[i][j];
        if (i) psum[i][j] += psum[i - 1][j];
        if (j) psum[i][j] += psum[i][j - 1];
        if (i and j) psum[i][j] -= psum[i - 1][j - 1];
      }

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        if (!grid[i][j] or (!i and !j) or (i == m - 1 and j == n - 1)) continue;
        int topright = (i ? psum[i - 1][n - 1] - psum[i - 1][j] : 0);
        int bottomleft = (j ? psum[m - 1][j - 1] - psum[i][j - 1] : 0);
        if (!topright and !bottomleft) return true;
      }
    return false;
  }
};
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
