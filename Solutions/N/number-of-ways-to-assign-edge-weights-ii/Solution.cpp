// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

const int nmax = 100000, mod = 1000000007;
vector<int> modpow;

class Solution {
public:
  vector<vector<int>> adj, par;
  vector<int> depth;

  vector<int> assignEdgeWeights(vector<vector<int>> &edges,
                                vector<vector<int>> &queries) {
    if (modpow.empty()) {
      modpow.push_back(1);
      for (int i = 0; i < nmax; ++i) {
        int x = modpow.back() << 1;
        if (x > mod)
          x -= mod;
        modpow.push_back(x);
      }
    }
    int n = edges.size() + 1;
    adj.resize(n);
    for (auto &e : edges) {
      int u = --e[0], v = --e[1];
      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    function<void(int, int)> dfs = [&](int u, int par) {
      for (int v : adj[u]) {
        if (v == par)
          continue;
        this->par[0][v] = u;
        depth[v] = depth[u] + 1;
        dfs(v, u);
      }
    };

    par = {vector<int>(n)};
    depth.resize(n);

    par[0][0] = -1;
    depth[0] = 0;
    dfs(0, -1);

    for (int i = 0, good = 1; good; ++i) {
      good = 0;
      par.push_back(vector<int>(n));
      for (int u = 0; u < n; ++u) {
        int pi = par[i][u];
        par[i + 1][u] = (pi == -1) ? -1 : par[i][pi];
        if (par[i + 1][u] != -1)
          good = 1;
      }
    }

    auto lca = [&](int u, int v) {
      if (depth[u] < depth[v])
        swap(u, v);
      int delta = depth[u] - depth[v];
      for (int i = par.size() - 1; i >= 0; --i)
        if (delta & (1 << i))
          u = par[i][u];
      if (u == v)
        return u;

      for (int i = par.size() - 1; i >= 0; --i)
        if (par[i][u] != par[i][v])
          u = par[i][u], v = par[i][v];
      return par[0][u];
    };

    vector<int> ret;
    for (auto &q : queries) {
      int u = --q[0], v = --q[1], w = lca(u, v);
      int d = depth[u] + depth[v] - 2 * depth[w];
      ret.push_back(d ? modpow[d - 1] : 0);
    }
    return ret;
  }
};
