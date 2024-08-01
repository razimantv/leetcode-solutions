# Find eventual safe states

[Problem link](https://leetcode.com/problems/find-eventual-safe-states/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-eventual-safe-states/

class Solution {
 public:
  vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
    int n = graph.size();

    // Reversed graph and outdegree count
    vector<vector<int>> rgraph(n);
    vector<int> outdegree(n);

    // node, next element to process in adjacency list
    stack<pair<int, int>> dfsstack;

    // Terminal nodes
    vector<int> ret;
    for (int u = 0; u < n; ++u) {
      // Add nodes without outdegree to stack and terminal node list
      if (!(outdegree[u] = graph[u].size())) {
        dfsstack.push({u, 0});
        ret.push_back(u);
      }

      // Reverse graph update
      for (int v : graph[u]) rgraph[v].push_back(u);
    }

    // Iterative depth first search
    while (!dfsstack.empty()) {
      auto& [u, pos] = dfsstack.top();

      // Check whether we have already processed all neighbours
      if (pos == rgraph[u].size()) {
        dfsstack.pop();
        continue;
      }

      // Process neighbour v and update position
      int v = rgraph[u][pos++];

      // If removing edge from v to u makes v terminal, add to stack
      if (!(--outdegree[v])) {
        dfsstack.push({v, 0});
        ret.push_back(v);
      }
    }

    sort(ret.begin(), ret.end());
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Topological sort](/Collections/graph-theory.md#topological-sort)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Iterative](/Collections/graph-theory.md#iterative)
* [Stack](/Collections/stack.md#stack) > [Depth first search](/Collections/stack.md#depth-first-search)
