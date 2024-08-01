# Is graph bipartite

[Problem link](https://leetcode.com/problems/is-graph-bipartite)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/is-graph-bipartite

class Solution {
 public:
  bool dfs(int u, const vector<vector<int>>& graph, vector<int>& colour) {
    for (int v : graph[u]) {
      if (colour[v] == colour[u])
        return false;
      else if (colour[v] + colour[u] == 3)
        continue;
      else {
        colour[v] = 3 - colour[u];
        if (!dfs(v, graph, colour)) return false;
      }
    }
    return true;
  }
  bool isBipartite(vector<vector<int>>& graph) {
    int N = graph.size();
    vector<int> colour(N, 0);

    for (int i = 0; i < N; ++i) {
      if (colour[i]) continue;

      colour[i] = 1;
      if (!dfs(i, graph, colour)) return false;
    }
    return true;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Colouring](/Collections/graph-theory.md#colouring)
