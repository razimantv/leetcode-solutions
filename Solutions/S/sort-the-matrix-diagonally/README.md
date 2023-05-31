# Sort the matrix diagonally

[Problem link](https://leetcode.com/problems/sort-the-matrix-diagonally)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-the-matrix-diagonally

class Solution {
 public:
  vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
    int m = mat.size(), n = mat[0].size();  // 0:m-1,0:n-1
    for (int d = 2 - n; d <= m - 2; ++d) {
      vector<int> cur;
      for (int i = max(0, d), j = i - d; i < m and j < n; ++i, ++j)
        cur.push_back(mat[i][j]);
      sort(cur.begin(), cur.end());
      for (int i = max(0, d), j = i - d, k = 0; i < m and j < n; ++i, ++j, ++k)
        mat[i][j] = cur[k];
    }
    return mat;
  }
};
```