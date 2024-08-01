# Min cost to connect all points

[Problem link](https://leetcode.com/problems/min-cost-to-connect-all-points)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/min-cost-to-connect-all-points

class Solution {
 public:
  vector<int> par;

  int parent(int u) { return (par[u] == u) ? u : (par[u] = parent(par[u])); }

  int minCostConnectPoints(vector<vector<int>>& points) {
    int P = points.size();
    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < P; ++i)
      for (int j = i + 1; j < P; ++j)
        edges.push_back({abs(points[i][0] - points[j][0]) +
                             abs(points[i][1] - points[j][1]),
                         i, j});
    sort(edges.begin(), edges.end());

    par.resize(P);
    iota(par.begin(), par.end(), 0);

    int ret = 0, done = 0;
    for (auto [w, u, v] : edges) {
      int uu = parent(u), vv = parent(v);
      if (uu == vv) continue;
      ret += w;
      par[uu] = vv;
      if (++done == P - 1) break;
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Minimum spanning tree](/Collections/graph-theory.md#minimum-spanning-tree)
* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
