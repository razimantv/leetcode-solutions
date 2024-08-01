# Difference between maximum and minimum price sum

[Problem link](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

class Solution {
 public:
  long long maxOutput(int n, vector<vector<int>>& edges, vector<int>& price) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    vector<long long> maxd(n);
    function<long long(int, int)> dfs = [&](int u, int par) {
      long long ret{};
      for (int v : adj[u])
        if (v != par) ret = max(ret, dfs(v, u));
      return maxd[u] = ret + price[u];
    };
    dfs(0, -1);

    function<long long(int, int, long long)> dfs2 = [&](int u, int par,
                                                        long long best) {
      long long ret = best;
      vector<pair<long long, int>> children;
      for (int v : adj[u]) {
        if (v == par) continue;
        children.push_back({maxd[v], v});
        ret = max(ret, maxd[v]);
      }

      int C = children.size();
      if (!C)
        return ret;
      else if (C > 1)
        partial_sort(children.begin(), children.begin() + 2, children.end(),
                     greater<pair<long long, int>>());

      for (int i = 0, C = children.size(); i < C; ++i) {
        auto [d, v] = children[i];
        long long newbest = best;
        if (i)
          newbest = max(newbest, children[0].first);
        else if (C > 1)
          newbest = max(newbest, children[1].first);
        newbest += price[u];

        ret = max(ret, dfs2(v, u, newbest));
      }
      return ret;
    };

    return dfs2(0, -1, 0);
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Sorting](/Collections/sorting.md#sorting) > [Stable](/Collections/sorting.md#stable)
