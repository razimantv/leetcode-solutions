# Minimum time to visit a cell in a grid

[Problem link](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution {
 public:
  int minimumTime(vector<vector<int>>& grid) {
    if (grid[0][1] > 1 and grid[1][0] > 1) return -1;
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dist(m, vector<int>(n, 1'000'000'000));
    auto cmp = [&](pair<int, int> u, pair<int, int> v) {
      if (dist[u.first][u.second] != dist[v.first][v.second])
        return dist[u.first][u.second] < dist[v.first][v.second];
      return u < v;
    };

    set<pair<int, int>, decltype(cmp)> djset(cmp);
    dist[0][0] = 0;
    djset.insert({0, 0});
    vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    while (!djset.empty()) {
      auto u = *djset.begin();
      djset.erase(djset.begin());
      auto [x, y] = u;
      for (auto [dx, dy] : neigh) {
        auto xx = x + dx, yy = y + dy;
        if (xx < 0 or xx >= m or yy < 0 or yy >= n) continue;
        int d = dist[x][y] + 1;
        if (d < grid[xx][yy]) d = grid[xx][yy] + ((grid[xx][yy] - d) & 1);
        if (d < dist[xx][yy]) {
          pair<int, int> v{xx, yy};
          if (djset.count(v)) djset.erase(v);
          dist[xx][yy] = d;
          djset.insert(v);
        }
      }
    }
    return dist[m - 1][n - 1];
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Dijkstra's algorithm](/Collections/priority-queue.md#dijkstra-s-algorithm)
