# Maximum strictly increasing cells in a matrix

[Problem link](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

class Solution {
 public:
  int maxIncreasingCells(vector<vector<int>>& mat) {
    map<int, vector<pair<int, int>>> valtopos;
    int m = mat.size(), n = mat[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) valtopos[mat[i][j]].push_back({i, j});
    vector<int> dpi(m), dpj(n);
    int ret{};
    for (auto [k, v] : valtopos) {
      int L = v.size();
      vector<int> best(L);
      for (int x = 0; x < L; ++x) {
        auto [i, j] = v[x];
        best[x] = max(dpi[i], dpj[j]) + 1;
      }
      for (int x = 0; x < L; ++x) {
        auto [i, j] = v[x];
        dpi[i] = max(dpi[i], best[x]);
        dpj[j] = max(dpj[j], best[x]);
        ret = max(ret, best[x]);
      }
    }

    return ret;
  }
};
```
## Tags

* [Matrix](/Collections/matrix.md#matrix)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Topological sort](/Collections/graph-theory.md#topological-sort)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Lewel-wise processing](/Collections/graph-theory.md#lewel-wise-processing)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
