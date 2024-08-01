# Number of operations to make network connected

[Problem link](https://leetcode.com/problems/number-of-operations-to-make-network-connected)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-operations-to-make-network-connected

class Solution {
 public:
  vector<vector<int>> adj;
  vector<char> seen;

  void dfs(int u) {
    seen[u] = 1;
    for (int v : adj[u])
      if (!seen[v]) dfs(v);
  }
  int makeConnected(int n, vector<vector<int>>& connections) {
    int E = connections.size();
    if (E < n - 1) return -1;

    adj.resize(n);
    seen.resize(n);
    for (const auto& e : connections)
      adj[e[0]].push_back(e[1]), adj[e[1]].push_back(e[0]);

    int ret = -1;
    for (int i = 0; i < n; ++i)
      if (!seen[i]) ++ret, dfs(i);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
