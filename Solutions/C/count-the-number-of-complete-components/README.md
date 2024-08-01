# Count the number of complete components

[Problem link](https://leetcode.com/problems/count-the-number-of-complete-components/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution {
 public:
  int countCompleteComponents(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    vector<char> seen(n);
    function<void(int, int&, int&)> dfs = [&](int u, int& vertices,
                                              int& edges) {
      seen[u] = 1;
      ++vertices;
      for (int v : adj[u]) {
        ++edges;
        if (!seen[v]) dfs(v, vertices, edges);
      }
    };

    int ret{};
    for (int u = 0; u < n; ++u) {
      if (seen[u]) continue;
      int vertices{}, edges{};
      dfs(u, vertices, edges);
      if (vertices * (vertices - 1) == edges) ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
