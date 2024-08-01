# Find critical and pseudo critical edges in minimum spanning tree

[Problem link](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

class Solution {
 public:
  int MST(int n, int m, vector<vector<int>>& edges, vector<int>& indices,
          int remove, vector<int>& pseudo) {
    vector<int> par(n);
    iota(par.begin(), par.end(), 0);
    function<int(int)> parent = [&](int u) {
      return (par[u] == u) ? u : (par[u] = parent(par[u]));
    };

    if (remove == -1) {
      for (int i = 0; i < m;) {
        auto& edgei = edges[indices[i]];
        for (int j = i; j < m; ++j) {
          auto& edgej = edges[indices[j]];
          if (edgej[2] != edgei[2]) break;
          int u = parent(edgej[0]), v = parent(edgej[1]);
          if (u != v) pseudo.push_back(indices[j]);
        }
        for (; i < m; ++i) {
          auto& edgej = edges[indices[i]];
          if (edgej[2] != edgei[2]) break;
          int u = parent(edgej[0]), v = parent(edgej[1]);
          par[u] = v;
        }
      }
      iota(par.begin(), par.end(), 0);
    }

    int len{}, comps{n};
    for (int ei : indices) {
      if (ei == remove) continue;
      auto& edge = edges[ei];
      int u = parent(edge[0]), v = parent(edge[1]);
      if (u != v) {
        par[u] = v;
        len += edge[2];
        --comps;
      }
    }
    return comps == 1 ? len : INT_MAX;
  }

  vector<vector<int>> findCriticalAndPseudoCriticalEdges(
      int n, vector<vector<int>>& edges) {
    int m = edges.size();
    vector<int> indices(m);
    iota(indices.begin(), indices.end(), 0);
    sort(indices.begin(), indices.end(),
         [&](int i, int j) { return edges[i][2] < edges[j][2]; });

    vector<int> critical, pseudo;
    int MSTlen = MST(n, m, edges, indices, -1, pseudo);
    if (MSTlen == INT_MAX) return {{}, {}};

    for (int i = 0; i < pseudo.size(); ++i) {
      if (MST(n, m, edges, indices, pseudo[i], pseudo) > MSTlen) {
        critical.push_back(pseudo[i]);
        swap(pseudo[i--], pseudo.back());
        pseudo.pop_back();
      }
    }
    return {critical, pseudo};
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Minimum spanning tree](/Collections/graph-theory.md#minimum-spanning-tree)
* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
