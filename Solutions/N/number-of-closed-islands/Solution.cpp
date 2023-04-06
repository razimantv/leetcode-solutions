// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
 public:
  int closedIsland(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size(), ret{};
    vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    function<bool(int, int)> dfs = [&](int i, int j) {
      bool good = true;
      grid[i][j] = 1;
      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj;
        if (ii < 0 or ii >= m or jj < 0 or jj >= n or
            (!grid[ii][jj] and !dfs(ii, jj)))
          good = false;
      }
      return good;
    };

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (!grid[i][j]) ret += dfs(i, j);
    return ret;
  }
};
