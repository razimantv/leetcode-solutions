# Shortest bridge

[Problem link](https://leetcode.com/problems/shortest-bridge/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-bridge/

class Solution {
 public:
  int m, n;
  const vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
  void dfs(vector<vector<int>>& grid, int i, int j, int c1, int c2) {
    grid[i][j] = c2;
    for (auto [di, dj] : neigh) {
      int ii = i + di, jj = j + dj;
      if (ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj] == c1)
        dfs(grid, ii, jj, c1, c2);
    }
  }
  int shortestBridge(vector<vector<int>>& grid) {
    m = grid.size(), n = grid[0].size();

    for (int i = 0, c = 2; i < m; ++i)
      for (int j = 0; j < n; ++j) {
        if (grid[i][j] == 1) dfs(grid, i, j, 1, c++);
      }

    vector<pair<int, int>> bfsq;
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j] == 2) bfsq.push_back({i, j});

    for (int x = 0; !bfsq.empty(); ++x) {
      vector<pair<int, int>> next;
      for (auto [i, j] : bfsq)
        for (auto [di, dj] : neigh) {
          int ii = i + di, jj = j + dj;
          if (ii < 0 or ii >= m or jj < 0 or jj >= n) continue;
          if (grid[ii][jj] == 3) return x;
          if (grid[ii][jj] == 0) {
            grid[ii][jj] = 2;
            next.push_back({ii, jj});
          }
        }
      bfsq = next;
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Flood fill](/Collections/graph-theory.md#flood-fill)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Multi source search](/Collections/graph-theory.md#multi-source-search)
