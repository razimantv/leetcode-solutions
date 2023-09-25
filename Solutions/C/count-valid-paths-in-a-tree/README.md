# Count valid paths in a tree

[Problem link](https://leetcode.com/problems/count-valid-paths-in-a-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

class Solution {
 public:
  long long countPaths(int n, vector<vector<int>>& edges) {
    vector<char> notprime(n + 1);
    notprime[1] = 1;
    for (int i = 2; i * i <= n; ++i) {
      if (notprime[i]) continue;
      for (int j = i * i; j <= n; j += i) notprime[j] = 1;
    }

    vector<vector<int>> adj(n + 1);
    for (const auto& e : edges) {
      int u = e[0], v = e[1];
      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    long long ret{};
    function<pair<int, int>(int, int)> dfs = [&](int u, int par) {
      bool prime = !notprime[u];
      int path1 = prime, path0 = 1 - path1;
      for (int v : adj[u]) {
        if (v == par) continue;
        auto [c1, c0] = dfs(v, u);
        ret += path1 * 1ll * c0 + path0 * 1ll * c1;
        if (prime) {
          path1 += c0;
        } else {
          path0 += c0;
          path1 += c1;
        }
      }
      return make_pair(path1, path0);
    };
    dfs(1, -1);
    return ret;
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/count-valid-paths-in-a-tree/

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        notprime = [0] * (n+1)
        notprime[1] = 1
        for i in range(2, n+1):
            if i*i > n:
                break
            if notprime[i]:
                continue
            for j in range(i*i, n+1, i):
                notprime[j] = 1

        ret = 0

        def dfs(u, par):
            nonlocal ret
            path0 = notprime[u]
            path1 = 1-path0

            for v in adj[u]:
                if v == par:
                    continue
                c0, c1 = dfs(v, u)
                ret += path0 * c1 + path1 * c0
                path0 += notprime[u] * c0
                path1 += notprime[u] * (c1 - c0) + c0
            return path0, path1

        dfs(1, 0)
        return ret
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees)
* [Graph theory](/README.md#Graph_theory) > [Depth first search](/README.md#Graph_theory-Depth_first_search)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Prime sieving](/README.md#Mathematics-Number_theory-Prime_sieving)
