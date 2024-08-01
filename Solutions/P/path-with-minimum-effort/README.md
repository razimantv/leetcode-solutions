# Path with minimum effort

[Problem link](https://leetcode.com/problems/path-with-minimum-effort)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/path-with-minimum-effort

class Solution {
 public:
  int minimumEffortPath(vector<vector<int>>& heights) {
    set<pair<int, pair<int, int>>> dist;
    set<pair<int, int>> seen;

    int m = heights.size(), n = heights[0].size(), best = 0;
    pair<int, int> end{m - 1, n - 1};
    int di[] = {0, 0, 1, -1}, dj[] = {1, -1, 0, 0};

    dist.insert({0, {0, 0}});
    while (!dist.empty()) {
      auto [w, ij] = *dist.begin();
      dist.erase(dist.begin());
      best = max(best, w);
      if (ij == end) break;
      seen.insert(ij);

      for (int k = 0; k < 4; ++k) {
        int ii = ij.first + di[k], jj = ij.second + dj[k];

        if (ii >= 0 and ii < m and jj >= 0 and jj < n and !seen.count({ii, jj}))
          dist.insert(
              {abs(heights[ii][jj] - heights[ij.first][ij.second]), {ii, jj}});
      }
    }
    return best;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
