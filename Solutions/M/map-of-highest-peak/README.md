# Map of highest peak

[Problem link](https://leetcode.com/problems/map-of-highest-peak/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/map-of-highest-peak/

class Solution {
public:
  vector<vector<int>> highestPeak(vector<vector<int>> &mat) {
    int m = mat.size(), n = mat[0].size();
    vector<vector<int>> ret(m, vector<int>(n, -1));
    queue<pair<int, int>> bfsq;

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (mat[i][j] == 1)
          ret[i][j] = 0, bfsq.push({i, j});

    vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    while (!bfsq.empty()) {
      auto [i, j] = bfsq.front();
      bfsq.pop();

      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj;
        if (ii >= 0 and ii < m and jj >= 0 and jj < n and ret[ii][jj] == -1)
          ret[ii][jj] = ret[i][j] + 1, bfsq.push({ii, jj});
      }
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
