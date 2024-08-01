# Add edges to make degrees of all nodes even

[Problem link](https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

class Solution {
 public:
  bool isPossible(int n, vector<vector<int>>& edges) {
    vector<int> deg(n);
    set<pair<int, int>> s;
    for (auto& e : edges) {
      int u = --e[0], v = --e[1];
      if (u > v) swap(u, v);
      ++deg[u];
      ++deg[v];
      s.insert({u, v});
    }

    vector<int> bad;
    for (int i = 0; i < n; ++i)
      if (deg[i] & 1) bad.push_back(i);

    if (bad.empty()) return true;
    if (bad.size() > 4) return false;
    if (bad.size() == 2) {
      if (!s.count({bad[0], bad[1]})) return true;
      set<int> s;
      for (auto e : edges) {
        if (e[0] == bad[0] or e[0] == bad[1]) s.insert(e[1]);
        if (e[1] == bad[1] or e[1] == bad[0]) s.insert(e[0]);
      }

      return s.size() < n;
    }
    vector<tuple<int, int, int, int>> poss{
        {0, 1, 2, 3}, {0, 2, 1, 3}, {0, 3, 1, 2}};
    for (auto [a, b, c, d] : poss)
      if (!s.count({bad[a], bad[b]}) and !s.count({bad[c], bad[d]}))
        return true;
    return false;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
