# Minimum edge weight equilibrium queries in a tree

[Problem link](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

class Solution {
 public:
  vector<vector<pair<int, int>>> adj;
  vector<vector<int>> par, psum;
  vector<int> depth;

  vector<int> minOperationsQueries(int n, vector<vector<int>>& edges,
                                   vector<vector<int>>& queries) {
    adj.resize(n);
    for (auto& e : edges) {
      int u = e[0], v = e[1], w = --e[2];
      adj[u].push_back({v, w});
      adj[v].push_back({u, w});
    }

    function<void(int, int)> dfs = [&](int u, int par) {
      for (auto [v, w] : adj[u]) {
        if (v == par) continue;
        this->par[0][v] = u;
        psum[v] = psum[u];
        ++psum[v][w];
        depth[v] = depth[u] + 1;
        dfs(v, u);
      }
    };

    par = {vector<int>(n)};
    psum.resize(n);
    depth.resize(n);

    par[0][0] = -1;
    psum[0].resize(26);
    depth[0] = 0;
    dfs(0, -1);

    for (int i = 0, good = 1; good; ++i) {
      good = 0;
      par.push_back(vector<int>(n));
      for (int u = 0; u < n; ++u) {
        int pi = par[i][u];
        par[i + 1][u] = (pi == -1) ? -1 : par[i][pi];
        if (par[i + 1][u] != -1) good = 1;
      }
    }

    auto lca = [&](int u, int v) {
      if (depth[u] < depth[v]) swap(u, v);
      int delta = depth[u] - depth[v];
      for (int i = par.size() - 1; i >= 0; --i)
        if (delta & (1 << i)) u = par[i][u];
      if (u == v) return u;

      for (int i = par.size() - 1; i >= 0; --i)
        if (par[i][u] != par[i][v]) u = par[i][u], v = par[i][v];
      return par[0][u];
    };

    vector<int> ret;
    for (auto& q : queries) {
      int u = q[0], v = q[1], w = lca(u, v);
      int tot = 0, maxval = 0;
      for (int i = 0; i < 26; ++i) {
        int cur = psum[u][i] + psum[v][i] - 2 * psum[w][i];
        tot += cur;
        maxval = max(maxval, cur);
      }
      ret.push_back(tot - maxval);
    }
    return ret;
  }
};
```
## Tags

* [Binary lifting](/Collections/binary-lifting.md#binary-lifting)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Lowest common ancestor](/Collections/graph-theory.md#lowest-common-ancestor)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
