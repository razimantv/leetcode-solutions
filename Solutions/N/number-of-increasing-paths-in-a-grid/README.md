# Number of increasing paths in a grid

[Problem link](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid

class Solution {
 public:
  unordered_map<int, int> cache;
  int M, N;
  const vector<pair<int, int>> neigh{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
  const int MOD = 1'000'000'007;

  int dfs(const vector<vector<int>>& grid, int x, int y) {
    int xy = (x << 17) | y;
    if (cache.count(xy)) return cache[xy];
    int& ans = cache[xy];
    ans = 1;
    for (auto [dx, dy] : neigh) {
      int xx = x + dx, yy = y + dy;
      if (xx >= 0 and yy >= 0 and xx < M and yy < N and
          grid[xx][yy] < grid[x][y]) {
        ans += dfs(grid, xx, yy);
        if (ans >= MOD) ans -= MOD;
      }
    }
    return ans;
  }
  int countPaths(vector<vector<int>>& grid) {
    M = grid.size(), N = grid[0].size();
    int ans = 0;
    for (int i = 0; i < M; ++i)
      for (int j = 0; j < N; ++j) {
        ans += dfs(grid, i, j);
        if (ans >= MOD) ans -= MOD;
      }
    return ans;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
