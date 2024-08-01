# Modify graph edge weights

[Problem link](https://leetcode.com/problems/modify-graph-edge-weights/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/modify-graph-edge-weights/

class Solution {
 public:
  vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges,
                                         int start, int end, int target) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto& e : edges) {
      int u = e[0], v = e[1], w = e[2];
      if (w == -1) continue;
      adj[u].push_back({v, w});
      adj[v].push_back({u, w});
    }

    vector<int> dist;
    auto cmp = [&](int u, int v) {
      return (dist[u] != dist[v]) ? (dist[u] < dist[v]) : u < v;
    };
    set<int, decltype(cmp)> djset(cmp);

    auto dijkstra = [&]() {
      dist = vector<int>(n, target + 1);
      djset.clear();
      dist[start] = 0;
      djset.insert(start);
      while (!djset.empty()) {
        int u = *djset.begin();
        djset.erase(djset.begin());
        if (u == end) return dist[end];
        for (auto [v, w] : adj[u]) {
          int newdist = dist[u] + w;
          if (newdist >= dist[v]) continue;
          if (djset.count(v)) djset.erase(v);
          dist[v] = newdist;
          djset.insert(v);
        }
      }
      return target + 1;
    };

    int x0 = dijkstra();
    if (x0 < target)
      return {};
    else if (x0 == target) {
      for (auto& e : edges)
        if (e.back() == -1) e.back() = target;
      return edges;
    }

    for (auto& e : edges) {
      int u = e[0], v = e[1], &w = e[2];
      if (w > 0) continue;
      w = 1;
      adj[u].push_back({v, w});
      adj[v].push_back({u, w});
      int x = dijkstra();
      // cout << x << "\n";
      if (x <= target) {
        w += target - x;
        for (auto& e2 : edges)
          if (e2.back() == -1) e2.back() = target;
        return edges;
      }
    }
    // cout << "\n";
    return {};
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Dijkstra's algorithm](/Collections/priority-queue.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
