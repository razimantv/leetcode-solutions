# Count number of possible root nodes

[Problem link](https://leetcode.com/problems/count-number-of-possible-root-nodes/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

class Solution {
 public:
  int rootCount(vector<vector<int>>& edges, vector<vector<int>>& guesses,
                int k) {
    int n = edges.size() + 1;
    vector<vector<int>> adj(n);
    vector<unordered_set<int>> guesschild(n);
    for (auto e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    for (auto g : guesses) guesschild[g[0]].insert(g[1]);

    vector<int> ancestordiff(n);
    int good{};
    function<void(int, int)> dfs = [&](int u, int par) {
      for (int v : adj[u]) {
        if (v == par) continue;
        ancestordiff[v] =
            ancestordiff[u] + guesschild[u].count(v) - guesschild[v].count(u);
        good += guesschild[u].count(v);
        dfs(v, u);
      }
    };

    dfs(0, -1);
    int ret{};
    for (int i = 0; i < n; ++i)
      if (good - ancestordiff[i] >= k) ++ret;
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
