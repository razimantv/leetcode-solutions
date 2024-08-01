# Minimize the total price of the trips

[Problem link](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

class Solution {
 public:
  int minimumTotalPrice(int n, vector<vector<int>>& edges, vector<int>& price,
                        vector<vector<int>>& trips) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    vector<int> cnt(n);
    function<bool(int, int, int)> dfs = [&](int u, int target, int par) {
      if (u == target) {
        ++cnt[u];
        return true;
      }

      for (int v : adj[u]) {
        if (v == par) continue;
        if (dfs(v, target, u)) {
          ++cnt[u];
          return true;
        }
      }
      return false;
    };

    for (auto trip : trips) dfs(trip[0], trip[1], -1);

    function<pair<int, int>(int, int)> dfs2 = [&](int u, int par) {
      int no = price[u] * cnt[u], yes = no / 2;
      for (int v : adj[u]) {
        if (v == par) continue;
        auto [cno, cyes] = dfs2(v, u);
        yes += cno;
        no += cyes;
      }
      yes = min(yes, no);
      return make_pair(no, yes);
    };
    return dfs2(0, -1).second;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
