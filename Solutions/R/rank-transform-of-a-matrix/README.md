# Rank transform of a matrix

[Problem link](https://leetcode.com/problems/rank-transform-of-a-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rank-transform-of-a-matrix

class Solution {
 public:
  pair<int, int> parent(pair<int, int> p, vector<vector<pair<int, int>>>& par) {
    if (par[p.first][p.second] == p)
      return p;
    else
      return par[p.first][p.second] = parent(par[p.first][p.second], par);
  }

  vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
    map<int, vector<pair<int, int>>> order;
    int m = matrix.size(), n = matrix[0].size();
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) order[matrix[i][j]].push_back({i, j});

    vector<vector<pair<int, int>>> par(m, vector<pair<int, int>>(n));
    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j) par[i][j] = {i, j};
    vector<vector<int>> best(m, vector<int>(n));

    vector<int> imax(m), jmax(n);
    for (auto& [val, vec] : order) {
      unordered_map<int, pair<int, int>> pari, parj;

      for (auto ij : vec) {
        auto [i, j] = ij;
        best[i][j] = max(imax[i], jmax[j]);

        if (!pari.count(i)) pari[i] = ij;
        if (!parj.count(j)) parj[j] = ij;
        pair<int, int> p = parent(ij, par), pi = parent(pari[i], par),
                       pj = parent(parj[j], par);
        best[p.first][p.second] =
            max(max(best[i][j], best[p.first][p.second]),
                max(best[pi.first][pi.second], best[pj.first][pj.second]));
        par[i][j] = par[pi.first][pi.second] = par[pj.first][pj.second] = p;
      }

      for (auto [i, j] : vec) {
        auto p = parent({i, j}, par);
        imax[i] = jmax[j] = matrix[i][j] = best[p.first][p.second] + 1;
      }
    }
    return matrix;
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
