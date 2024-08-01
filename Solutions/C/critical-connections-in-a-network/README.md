# Critical connections in a network

[Problem link](https://leetcode.com/problems/critical-connections-in-a-network)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/critical-connections-in-a-network

class Solution {
 public:
  vector<vector<int>> adj, bridges;
  vector<tuple<int, int, int, int>> PNLH;
  int next;
  void dfs(int u, int par) {
    auto& [P, N, L, H] = PNLH[u];
    P = ++next;
    N = 1;
    L = H = P;
    for (int v : adj[u]) {
      if (v == par) continue;
      auto& [Pv, Nv, Lv, Hv] = PNLH[v];
      if (!Pv) {
        dfs(v, u);
        N += Nv;
        if (Lv == Pv and Hv < Pv + Nv) bridges.push_back({u, v});
      }
      L = min(L, Lv);
      H = max(H, Hv);
    }
  }

  vector<vector<int>> criticalConnections(int n, vector<vector<int>>& edges) {
    adj.resize(n);
    PNLH.resize(n);
    next = 0;

    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    dfs(0, -1);
    return bridges;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Bridges/Articulation points](/Collections/graph-theory.md#bridges-articulation-points)
