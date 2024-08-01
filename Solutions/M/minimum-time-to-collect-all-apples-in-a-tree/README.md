# Minimum time to collect all apples in a tree

[Problem link](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution {
 public:
  int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
    vector<vector<int>> adj(n);
    for (const auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    std::function<pair<bool, int>(int, int)> dfs = [&](int u, int par) {
      pair<bool, int> ret;
      auto& [flag, tot] = ret;

      flag = hasApple[u];
      for (int v : adj[u]) {
        if (v == par) continue;
        auto [cf, ct] = dfs(v, u);
        if (cf) {
          flag = true;
          tot += ct + 2;
        }
      }
      return ret;
    };

    return dfs(0, -1).second;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
