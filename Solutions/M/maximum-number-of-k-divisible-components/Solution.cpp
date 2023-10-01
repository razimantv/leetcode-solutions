// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution {
 public:
  int maxKDivisibleComponents(int n, vector<vector<int>>& edges,
                              vector<int>& values, int k) {
    vector<vector<int>> adj(n);
    for (auto edge : edges) {
      int u = edge[0], v = edge[1];
      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    function<pair<int, int>(int, int)> dfs = [&](int u, int par) {
      int tot{values[u] % k}, cnt{};
      for (int v : adj[u]) {
        if (v == par) continue;
        auto [ctot, ccnt] = dfs(v, u);
        cnt += ccnt + !ctot;
        tot = (tot + ctot) % k;
      }
      return make_pair(tot, cnt);
    };
    return dfs(0, -1).second + 1;
  }
};
