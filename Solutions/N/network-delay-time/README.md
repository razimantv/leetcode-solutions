# Network delay time

[Problem link](https://leetcode.com/problems/network-delay-time)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/network-delay-time

class Solution {
 public:
  int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto& edge : times) adj[--edge[0]].push_back({--edge[1], edge[2]});

    vector<int> dist(n, INT_MAX);
    vector<char> seen(n);
    auto cmp = [&](int x, int y) {
      if (dist[x] != dist[y]) return dist[x] < dist[y];
      return x < y;
    };
    set<int, decltype(cmp)> djset(cmp);
    dist[--k] = 0;
    djset.insert(k);

    int ret = 0, cnt = 0;
    while (!djset.empty()) {
      int u = *djset.begin();
      djset.erase(djset.begin());
      ret = max(ret, dist[u]);
      seen[u] = 1;
      ++cnt;

      for (auto [v, w] : adj[u]) {
        if (seen[v]) continue;
        int newdist = dist[u] + w;
        if (newdist >= dist[v]) continue;
        if (djset.count(v)) djset.erase(v);
        dist[v] = newdist;
        djset.insert(v);
      }
    }
    return (cnt == n) ? ret : -1;
  }
};
```
## Tags

* [Priority queue](/README.md#Priority_queue) > [Dijkstra's algorithm](/README.md#Priority_queue-Dijkstra_s_algorithm)
* [Priority queue](/README.md#Priority_queue) > [Key update using insert and remove on C++ set](/README.md#Priority_queue-Key_update_using_insert_and_remove_on_C___set)
* [Graph theory](/README.md#Graph_theory) > [Dijkstra's algorithm](/README.md#Graph_theory-Dijkstra_s_algorithm)
