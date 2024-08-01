# Redundant connection

[Problem link](https://leetcode.com/problems/redundant-connection)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/redundant-connection

class Solution {
 public:
  vector<int> par;
  int parent(int a) { return par[a] == a ? a : (par[a] = parent(par[a])); }
  vector<int> findRedundantConnection(vector<vector<int>>& edges) {
    int N = edges.size();
    par.resize(N);
    iota(par.begin(), par.end(), 0);

    for (auto& e : edges) {
      int a = e[0], b = e[1], u = parent(a - 1), v = parent(b - 1);
      if (u == v) return {a, b};
      par[u] = v;
    }
    return {-1, -1};
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
