# Last day where you can still cross

[Problem link](https://leetcode.com/problems/last-day-where-you-can-still-cross/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution {
 public:
  vector<pair<int, int>> neigh{{0, 1}, {1, 0},  {0, -1},  {-1, 0},
                               {1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
  int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
    struct dsu {
      int parent, left, right;
    };
    vector<dsu> par;
    function<int(int)> parent = [&](int u) {
      int& uu = par[u].parent;
      return (uu == u) ? u : (uu = parent(uu));
    };
    vector<vector<int>> seen(row, vector<int>(col, -1));
    for (int i = 0, n = cells.size(); i < n; ++i) {
      int x = cells[i][0] - 1, y = cells[i][1] - 1;
      seen[x][y] = i;
      par.push_back({i, y, y});
      for (auto [di, dj] : neigh) {
        int ii = x + di, jj = y + dj;
        if (ii < 0 or ii >= row or jj < 0 or jj >= col or seen[ii][jj] == -1)
          continue;
        int u = parent(seen[ii][jj]);
        par[u].parent = i;
        par[i].left = min(par[i].left, par[u].left);
        par[i].right = max(par[i].right, par[u].right);
        if (par[i].left == 0 and par[i].right == col - 1) return i;
      }
    }
    return -1;
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
