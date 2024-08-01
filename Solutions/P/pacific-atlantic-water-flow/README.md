# Pacific atlantic water flow

[Problem link](https://leetcode.com/problems/pacific-atlantic-water-flow)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution {
 public:
  vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
    if (matrix.empty()) return {};
    int M = matrix.size(), N = matrix[0].size();
    pair<int, int> neigh[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    vector<vector<char>> cnt(M, vector<char>(N, 0));
    vector<vector<int>> ret;
    for (int n = 0; n < 2; ++n) {
      queue<pair<int, int>> bfsq;
      for (int i = 0; i < N; ++i) {
        bfsq.push({n * (M - 1), i});
        cnt[n * (M - 1)][i] |= (1 << n);
      }
      for (int i = 0; i < M - 1; ++i) {
        bfsq.push({i + 1 - n, n * (N - 1)});
        cnt[i + 1 - n][n * (N - 1)] |= (1 << n);
      }

      while (!bfsq.empty()) {
        auto [i, j] = bfsq.front();
        bfsq.pop();
        if (cnt[i][j] == 3) ret.push_back({i, j});
        for (auto [di, dj] : neigh) {
          int ii = i + di, jj = j + dj;
          if (ii < 0 or ii >= M or jj < 0 or jj >= N or
              (cnt[ii][jj] & (1 << n)) or matrix[ii][jj] < matrix[i][j])
            continue;
          bfsq.push({ii, jj});
          cnt[ii][jj] |= (1 << n);
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
