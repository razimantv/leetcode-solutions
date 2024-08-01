# Max area of island

[Problem link](https://leetcode.com/problems/max-area-of-island)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/max-area-of-island

class Solution {
 public:
  int m, n;
  int dfs(vector<vector<int>>& grid, int i, int j) {
    int cnt = 1;
    grid[i][j] = 0;
    int neigh[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for (auto [di, dj] : neigh) {
      int ii = i + di, jj = j + dj;
      if (ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj])
        cnt += dfs(grid, ii, jj);
    }
    return cnt;
  }
  int maxAreaOfIsland(vector<vector<int>>& grid) {
    int best = 0;
    m = grid.size(), n = grid[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j]) best = max(best, dfs(grid, i, j));
    return best;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Flood fill](/Collections/graph-theory.md#flood-fill)
