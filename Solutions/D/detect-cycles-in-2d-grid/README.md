# Detect cycles in 2d grid

[Problem link](https://leetcode.com/problems/detect-cycles-in-2d-grid)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/detect-cycles-in-2d-grid

class Solution {
 public:
  int m, n;
  const vector<pair<int, int>> neigh{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

  bool dfs(int r, int c, int fromr, int fromc, vector<vector<char>>& grid,
           vector<vector<char>>& seen) {
    seen[r][c] = true;
    for (auto [dr, dc] : neigh) {
      int tor = r + dr, toc = c + dc;
      if (tor < 0 or tor >= m or toc < 0 or toc >= n or
          grid[r][c] != grid[tor][toc] or
          (tor == fromr and toc == fromc))  // Don't do DFS to parent
        continue;

      // If a non-parent neighbour has been visited, you have a cycle
      if (seen[tor][toc] or dfs(tor, toc, r, c, grid, seen)) return true;
    }
    return false;
  }
  bool containsCycle(vector<vector<char>>& grid) {
    m = grid.size(), n = grid[0].size();
    vector<vector<char>> seen(m, vector<char>(n));

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (!seen[i][j] and dfs(i, j, -1, -1, grid, seen)) return true;

    return false;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
