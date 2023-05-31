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

* [Matrix](/README.md#Matrix)
* [Graph theory](/README.md#Graph_theory) > [Topological sort](/README.md#Graph_theory-Topological_sort)
* [Graph theory](/README.md#Graph_theory) > [Lewel-wise processing](/README.md#Graph_theory-Lewel_wise_processing)
* [Dynamic programming](/README.md#Dynamic_programming)
