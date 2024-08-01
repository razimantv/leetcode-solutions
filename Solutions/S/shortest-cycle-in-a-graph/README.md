# Shortest cycle in a graph

[Problem link](https://leetcode.com/problems/shortest-cycle-in-a-graph/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

class Solution {
 public:
  int findShortestCycle(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    vector<char> seen(n);
    vector<int> depth(n);
    int ret = n + 1;
    function<void(int, int)> dfs = [&](int u, int par) {
      for (int v : adj[u]) {
        if (v == par) continue;
        if (seen[v] == seen[u]) {
          ret = min(ret, abs(depth[u] - depth[v]) + 1);
          continue;
        }
        seen[v] = seen[u];
        depth[v] = depth[u] + 1;
        dfs(v, u);
      }
    };

    for (int u = 0; u < n; ++u) {
      seen[u] = u + 1;
      depth[u] = 0;
      dfs(u, -1);
    }

    return ret > n ? -1 : ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Reuse visited array](/Collections/graph-theory.md#reuse-visited-array)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
