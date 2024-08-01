# Reorder routes to make all paths lead to the city zero

[Problem link](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution {
 public:
  int minReorder(int n, vector<vector<int>>& connections) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto e : connections) {
      adj[e[0]].push_back({e[1], 1});
      adj[e[1]].push_back({e[0], 0});
    }

    function<int(int, int)> dfs = [&](int u, int par) {
      int ret{};
      for (auto [v, dir] : adj[u]) {
        if (v == par) continue;
        ret += dir + dfs(v, u);
      }
      return ret;
    };
    return dfs(0, -1);
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
