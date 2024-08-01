# Minimum number of visited cells in a grid

[Problem link](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

class Solution {
 public:
  int minimumVisitedCells(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dist(m, vector<int>(n, -1));
    vector<int> tempi(n), tempj(m);
    iota(tempi.begin(), tempi.end(), 0);
    iota(tempj.begin(), tempj.end(), 0);
    vector<set<int>> remi(m, set<int>(tempi.begin(), tempi.end())),
        remj(n, set<int>(tempj.begin(), tempj.end()));

    queue<pair<int, int>> bfsq;
    bfsq.push({0, 0});
    dist[0][0] = 1;
    remi[0].erase(0);
    remj[0].erase(0);

    while (!bfsq.empty()) {
      auto [i, j] = bfsq.front();
      bfsq.pop();
      int jmax = min(j + grid[i][j], n - 1);
      for (auto sit = remi[i].upper_bound(j);
           sit != remi[i].end() and *sit <= jmax; remi[i].erase(sit++)) {
        int jj = *sit;
        dist[i][jj] = dist[i][j] + 1;
        if (i == m - 1 and jj == n - 1) return dist[i][jj];
        remj[jj].erase(i);
        bfsq.push({i, jj});
      }

      int imax = min(i + grid[i][j], m - 1);
      for (auto sit = remj[j].upper_bound(i);
           sit != remj[j].end() and *sit <= imax; remj[j].erase(sit++)) {
        int ii = *sit;
        dist[ii][j] = dist[i][j] + 1;
        if (ii == m - 1 and j == n - 1) return dist[ii][j];
        remi[ii].erase(j);
        bfsq.push({ii, j});
      }
    }

    return dist.back().back();
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
