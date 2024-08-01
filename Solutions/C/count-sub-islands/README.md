# Count sub islands

[Problem link](https://leetcode.com/problems/count-sub-islands)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-sub-islands

class Solution {
 public:
  const int neigh[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
  int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
    int M = grid1.size(), N = grid1[0].size(), ret = 0;
    for (int i = 0; i < M; ++i)
      for (int j = 0; j < N; ++j) {
        if (!grid2[i][j]) continue;
        vector<pair<int, int>> stk;
        stk.push_back({i, j});
        bool flag = grid1[i][j];
        grid2[i][j] = 0;
        while (!stk.empty()) {
          auto [x, y] = stk.back();
          stk.pop_back();
          for (auto [dx, dy] : neigh) {
            int xx = x + dx, yy = y + dy;
            if (xx >= 0 and xx < M and yy >= 0 and yy < N and grid2[xx][yy]) {
              grid2[xx][yy] = 0;
              stk.push_back({xx, yy});
              flag &= grid1[xx][yy];
            }
          }
        }
        if (flag) ++ret;
      }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Flood fill](/Collections/graph-theory.md#flood-fill)
