# Find the safest path in a grid

[Problem link](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution {
 public:
  int maximumSafenessFactor(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();

    queue<pair<int, int>> bfsq;
    vector<vector<pair<int, int>>> distwise(1);
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j]) {
          bfsq.push({i, j});
          distwise[0].push_back({i, j});
        }
    const vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    while (!bfsq.empty()) {
      auto [i, j] = bfsq.front();
      bfsq.pop();
      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj;
        if (ii >= 0 and ii < m and jj >= 0 and jj < n and !grid[ii][jj]) {
          grid[ii][jj] = grid[i][j] + 1;
          if (distwise.size() == grid[i][j]) distwise.push_back({});
          distwise[grid[i][j]].push_back({ii, jj});
          bfsq.push({ii, jj});
        }
      }
    }

    vector<vector<pair<int, int>>> parent(m,
                                          vector<pair<int, int>>(n, {-1, -1}));

    function<pair<int, int>(pair<int, int>)> par = [&](pair<int, int> u) {
      auto& v = parent[u.first][u.second];
      return u == v ? u : (v = par(v));
    };

    pair<int, int> start{0, 0}, end{m - 1, n - 1};
    for (int L = distwise.size(), d = L - 1; d >= 0; --d) {
      for (auto u : distwise[d]) {
        parent[u.first][u.second] = u;
        auto [i, j] = u;
        for (auto [di, dj] : neigh) {
          int ii = i + di, jj = j + dj;
          if (ii >= 0 and ii < m and jj >= 0 and jj < n and
              parent[ii][jj].first != -1) {
            auto v = par({ii, jj});
            parent[v.first][v.second] = u;
          }
        }
        if (parent[0][0].first != -1 and parent[m - 1][n - 1].first != -1 and
            par(start) == par(end))
          return d;
      }
    }
    return 0;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Multi source search](/Collections/graph-theory.md#multi-source-search)
* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
