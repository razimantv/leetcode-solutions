# Largest color value in a directed graph

[Problem link](https://leetcode.com/problems/largest-color-value-in-a-directed-graph)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph

class Solution {
 public:
  int largestPathValue(string colors, vector<vector<int>>& edges) {
    int n = colors.size();
    vector<vector<int>> adj(n);
    vector<int> indegree(n);
    for (auto& e : edges) {
      indegree[e[1]]++;
      adj[e[0]].push_back(e[1]);
    }
    vector<int> todo, toposort;
    for (int i = 0; i < n; ++i)
      if (indegree[i] == 0) todo.push_back(i);
    while (!todo.empty()) {
      int u = todo.back();
      todo.pop_back();

      toposort.push_back(u);
      for (int v : adj[u]) {
        if (--indegree[v] == 0) todo.push_back(v);
      }
    }

    if (toposort.size() < n) return -1;

    vector<vector<int>> best(n, vector<int>(26));
    int ret = 0;
    for (int i = n - 1; i >= 0; --i) {
      int u = toposort[i];
      for (int v : adj[u]) {
        for (int c = 0; c < 26; ++c) best[u][c] = max(best[u][c], best[v][c]);
      }
      ret = max(ret, ++best[u][colors[u] - 'a']);
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/README.md#Graph_theory) > [Topological sort](/README.md#Graph_theory-Topological_sort) > [Dynamic Programming](/README.md#Graph_theory-Topological_sort-Dynamic_Programming)
* [Dynamic programming](/README.md#Dynamic_programming) > [Topological sort](/README.md#Dynamic_programming-Topological_sort)
