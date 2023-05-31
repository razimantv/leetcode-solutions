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

* [Graph theory](/README.md#Graph_theory) > [Topological sort](/README.md#Graph_theory-Topological_sort)
* [Graph theory](/README.md#Graph_theory) > [Depth first search](/README.md#Graph_theory-Depth_first_search) > [Iterative](/README.md#Graph_theory-Depth_first_search-Iterative)
* [Stack](/README.md#Stack) > [Depth first search](/README.md#Stack-Depth_first_search)
