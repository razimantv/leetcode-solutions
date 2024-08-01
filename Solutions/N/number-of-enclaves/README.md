# Number of enclaves

[Problem link](https://leetcode.com/problems/number-of-enclaves/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-enclaves/

class Solution {
 public:
  int numEnclaves(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size(), ret{};
    vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    function<int(int, int)> dfs = [&](int i, int j) {
      int cnt = 1;
      grid[i][j] = 0;
      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj, x;
        if (ii < 0 or ii >= m or jj < 0 or jj >= n)
          cnt = 0;
        else if (grid[ii][jj]) {
          int x = dfs(ii, jj);
          if (x and cnt)
            cnt += x;
          else
            cnt = 0;
        }
      }
      return cnt;
    };

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j]) ret += dfs(i, j);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Flood fill](/Collections/graph-theory.md#flood-fill)
