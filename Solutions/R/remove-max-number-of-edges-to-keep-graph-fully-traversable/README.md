# Remove max number of edges to keep graph fully traversable

[Problem link](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable

class Solution {
 public:
  int parent(int u, vector<int>& par) {
    return par[u] == u ? u : (par[u] = parent(par[u], par));
  }
  int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(),
         [&](const auto& u, const auto& v) { return u[0] > v[0]; });
    vector<int> alice(n);
    iota(alice.begin(), alice.end(), 0);
    auto bob = alice;
    int comp1 = n - 1, comp2 = n - 1, remove = edges.size();
    for (auto e : edges) {
      int type = e[0], u = --e[1], v = --e[2], cur = 0;
      if (type & 1) {
        int uu = parent(u, alice), vv = parent(v, alice);
        if (uu != vv) {
          --comp1;
          cur = 1;
          alice[vv] = uu;
        }
      }
      if (type & 2) {
        int uu = parent(u, bob), vv = parent(v, bob);
        if (uu != vv) {
          --comp2;
          cur = 1;
          bob[vv] = uu;
        }
      }

      remove -= cur;
    }

    if (comp1 or comp2) return -1;
    return remove;
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
