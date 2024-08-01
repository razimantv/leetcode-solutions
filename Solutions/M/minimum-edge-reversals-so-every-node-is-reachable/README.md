# Minimum edge reversals so every node is reachable

[Problem link](https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

class Solution {
 public:
  vector<int> minEdgeReversals(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto edge : edges) {
      int u = edge[0], v = edge[1];
      adj[u].push_back({v, 0});
      adj[v].push_back({u, 1});
    }

    vector<int> ret(n);
    function<int(int, int)> dfs = [&](int u, int par) {
      int cur{};
      for (auto [v, dir] : adj[u]) {
        if (v == par) continue;
        cur += dir + dfs(v, u);
      }
      return cur;
    };
    ret[0] = dfs(0, -1);

    function<void(int, int)> dfs2 = [&](int u, int par) {
      for (auto [v, dir] : adj[u]) {
        if (v == par) continue;
        ret[v] = ret[u] - (2 * dir - 1);
        dfs2(v, u);
      }
    };
    dfs2(0, -1);

    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
