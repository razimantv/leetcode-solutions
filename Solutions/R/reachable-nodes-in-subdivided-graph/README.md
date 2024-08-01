# Reachable nodes in subdivided graph

[Problem link](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph

class Solution {
 public:
  int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto& e : edges) {
      adj[e[0]].push_back({e[1], e[2]});
      adj[e[1]].push_back({e[0], e[2]});
    }

    vector<int> remain(n, -1);
    auto cmp = [&](int u, int v) {
      return remain[u] == remain[v] ? u < v : remain[u] > remain[v];
    };
    set<int, decltype(cmp)> dj(cmp);
    vector<char> seen(n);

    remain[0] = maxMoves;
    dj.insert(0);

    int ret = 0;
    while (!dj.empty()) {
      int u = *dj.begin();
      dj.erase(dj.begin());
      seen[u] = true;
      ++ret;

      for (auto [v, w] : adj[u]) {
        if (seen[v] or remain[v] >= remain[u] - w - 1) continue;
        if (dj.count(v)) dj.erase(v);
        remain[v] = remain[u] - w - 1;
        dj.insert(v);
      }
    }

    for (auto& e : edges) {
      int &u = e[0], &v = e[1], &w = e[2];
      ret += min(max(0, remain[u]) + max(0, remain[v]), w);
    }

    return ret;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
