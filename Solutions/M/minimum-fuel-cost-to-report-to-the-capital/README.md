# Minimum fuel cost to report to the capital

[Problem link](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution {
 public:
  vector<vector<int>> adj;
  long long ret;
  int dfs(int u, int seats, int par = -1) {
    int tot = 1;
    for (int v : adj[u]) {
      if (v == par) continue;
      int cur = dfs(v, seats, u);
      ret += (cur + seats - 1) / seats;
      tot += cur;
    }
    return tot;
  }
  long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
    int n = roads.size() + 1;
    adj.resize(n);
    for (auto& e : roads) {
      int u = e[0], v = e[1];
      adj[u].push_back(v);
      adj[v].push_back(u);
    }
    ret = 0;
    dfs(0, seats);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
