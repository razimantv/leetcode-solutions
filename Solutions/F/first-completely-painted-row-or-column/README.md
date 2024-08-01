# First completely painted row or column

[Problem link](https://leetcode.com/problems/first-completely-painted-row-or-column/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
 public:
  int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
    int m = mat.size(), n = mat[0].size();
    unordered_map<int, pair<int, int>> pos(m * n);
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) pos[mat[i][j]] = {i, j};

    vector<int> row(m), col(n);
    for (int i = 0; i < m * n; ++i) {
      auto [r, c] = pos[arr[i]];
      if (++row[r] == n or ++col[c] == m) return i;
    }
    return -1;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
