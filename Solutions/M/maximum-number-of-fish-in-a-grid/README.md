# Maximum number of fish in a grid

[Problem link](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution {
 public:
  int findMaxFish(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    const int neigh[4][2]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    function<int(int, int)> dfs = [&](int i, int j) {
      int ret = grid[i][j];
      grid[i][j] = 0;
      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj;
        if (ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj])
          ret += dfs(ii, jj);
      }
      return ret;
    };

    int ret{};
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j]) ret = max(ret, dfs(i, j));
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Flood fill](/Collections/graph-theory.md#flood-fill)
