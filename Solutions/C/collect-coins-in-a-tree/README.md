# Collect coins in a tree

[Problem link](https://leetcode.com/problems/collect-coins-in-a-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/collect-coins-in-a-tree/

class Solution {
 public:
  int collectTheCoins(vector<int>& coins, vector<vector<int>>& edges) {
    int n = coins.size();
    if (n <= 5) return 0;
    vector<vector<int>> adj(n);
    vector<int> degree(n);
    for (auto e : edges) {
      int u = e[0], v = e[1];
      adj[u].push_back(v);
      adj[v].push_back(u);
      ++degree[u];
      ++degree[v];
    }

    auto get_toremove = [&](int limit) {
      vector<int> ret;
      for (int i = 0; i < n; ++i)
        if (coins[i] < limit and degree[i] == 1) ret.push_back(i);
      return ret;
    };
    auto toremove = get_toremove(1);

    int remaining = n;
    auto process = [&](vector<int>& cur, vector<int>& next, int limit) {
      while (!cur.empty()) {
        --remaining;
        int u = cur.back();
        cur.pop_back();
        degree[u] = 0;
        for (int v : adj[u]) {
          if (!degree[v]) continue;
          --degree[v];
          if (coins[v] < limit and degree[v] == 1) next.push_back(v);
        }
      }
    };

    process(toremove, toremove, 1);
    if (remaining <= 5) return 0;

    toremove = get_toremove(2);
    for (int i = 0; i < 2; ++i) {
      vector<int> next;
      process(toremove, next, 2);
      toremove = next;
    }

    return max(remaining - 1, 0) * 2;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Iterative leaf removal](/Collections/graph-theory.md#iterative-leaf-removal)
