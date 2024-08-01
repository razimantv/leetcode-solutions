# Count unreachable pairs of nodes in an undirected graph

[Problem link](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph

class Solution {
 public:
  vector<char> seen;
  vector<vector<int>> adj;

  int dfs(int u) {
    int cur = seen[u] = 1;
    for (int v : adj[u])
      if (!seen[v]) cur += dfs(v);
    return cur;
  }
  long long countPairs(int n, vector<vector<int>>& edges) {
    adj.resize(n);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }
    long long ret = n * (long long)(n - 1) / 2;
    seen = vector<char>(n);
    for (int i = 0; i < n; ++i) {
      if (!seen[i]) {
        int cur = dfs(i);
        ret -= cur * (long long)(cur - 1) / 2;
      }
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
