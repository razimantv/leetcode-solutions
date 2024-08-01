# Find edges in shortest paths

[Problem link](https://leetcode.com/problems/find-edges-in-shortest-paths/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-edges-in-shortest-paths/

class Solution {
 public:
  vector<bool> findAnswer(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto& e : edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].push_back({v, w});
      adj[v].push_back({u, w});
    }
    auto inf = 1ll << 50;

    auto dijkstra = [&](int start) {
      vector<long long> dist(n, inf);
      auto cmp = [&](int u, int v) {
        return make_pair(dist[u], u) < make_pair(dist[v], v);
      };
      set<int, decltype(cmp)> djset(cmp);

      dist[start] = 0;
      djset.insert(start);
      while (!djset.empty()) {
        int u = *djset.begin();
        djset.erase(djset.begin());
        for (auto [v, w] : adj[u]) {
          auto vdist = dist[u] + w;
          if (vdist < dist[v]) {
            if (djset.count(v)) djset.erase(v);
            dist[v] = vdist;
            djset.insert(v);
          }
        }
      }
      return dist;
    };

    auto dist1 = dijkstra(0);
    int m = edges.size();
    if (dist1[n - 1] == inf) return vector<bool>(m);
    auto dist2 = dijkstra(n - 1);
    vector<bool> ret;
    for (auto& e : edges) {
      int u = e[0], v = e[1], w = e[2];
      ret.push_back(min(dist1[u] + dist2[v], dist1[v] + dist2[u]) + w ==
                    dist2[0]);
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm) > [Forward and backward](/Collections/graph-theory.md#forward-and-backward)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
