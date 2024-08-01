# Maximal network rank

[Problem link](https://leetcode.com/problems/maximal-network-rank/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximal-network-rank/

class Solution {
 public:
  int maximalNetworkRank(int n, vector<vector<int>>& roads) {
    vector<vector<int>> adj(n, vector<int>(n));
    for (auto& e : roads) {
      int u = e[0], v = e[1];
      ++adj[u][v];
      ++adj[v][u];
    }

    int best{};
    auto rank = [&](int u, int v) {
      return accumulate(adj[u].begin(), adj[u].end(), 0) +
             accumulate(adj[v].begin(), adj[v].end(), 0) - adj[u][v];
    };
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < i; ++j) best = max(best, rank(i, j));
    return best;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory)
