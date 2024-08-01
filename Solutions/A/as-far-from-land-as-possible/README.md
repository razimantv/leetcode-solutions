# As far from land as possible

[Problem link](https://leetcode.com/problems/as-far-from-land-as-possible/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution {
 public:
  int maxDistance(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> bfsq;
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j]) bfsq.push({i, j});

    int ret{0};
    while (!bfsq.empty()) {
      auto [u, v] = bfsq.front();
      bfsq.pop();
      const vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
      for (auto [du, dv] : neigh) {
        int uu = u + du, vv = v + dv;
        if (uu >= 0 and uu < m and vv >= 0 and vv < n and !grid[uu][vv]) {
          grid[uu][vv] = ret = grid[u][v] + 1;
          bfsq.push({uu, vv});
        }
      }
    }
    return ret - 1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Multi source search](/Collections/graph-theory.md#multi-source-search)
