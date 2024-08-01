# Maximum number of points from grid queries

[Problem link](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

class Solution {
 public:
  vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
    using coord = pair<int, int>;
    auto cmp = [&](const coord& c1, const coord& c2) {
      auto [x1, y1] = c1;
      auto [x2, y2] = c2;
      if (grid[x1][y1] != grid[x2][y2]) return grid[x1][y1] < grid[x2][y2];
      return c1 < c2;
    };

    set<coord, decltype(cmp)> prim(cmp);
    map<int, int, greater<int>> best;
    prim.insert({0, 0});
    best[0] = 0;

    int large{}, tot{};
    while (!prim.empty()) {
      auto [i, j] = *prim.begin();
      prim.erase(prim.begin());

      large = max(large, grid[i][j]);
      ++tot;
      grid[i][j] = 0;
      best[large] = tot;

      int m = grid.size(), n = grid[0].size();
      for (auto [di, dj] : vector<coord>({{0, 1}, {1, 0}, {0, -1}, {-1, 0}})) {
        int ii = i + di, jj = j + dj;
        if (ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj])
          prim.insert({ii, jj});
      }
    }

    for (int& q : queries) q = best.upper_bound(q)->second;
    return queries;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Prim's algorithm](/Collections/graph-theory.md#prim-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
