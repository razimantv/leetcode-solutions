# Number of ways to arrive at destination

[Problem link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

class Solution {
 public:
  int countPaths(int n, vector<vector<int>>& roads) {
    vector<vector<pair<int, int>>> adj(n);
    for (auto& e : roads) {
      adj[e[0]].push_back({e[1], e[2]});
      adj[e[1]].push_back({e[0], e[2]});
    }

    unordered_map<int, pair<long long, int>> dist_ways;
    auto cmp = [&](int u, int v) {
      long long distdiff = dist_ways[u].first - dist_ways[v].first;
      return distdiff ? (distdiff < 0) : (u < v);
    };
    set<int, decltype(cmp)> djset(cmp);
    dist_ways[0] = {0, 1};
    djset.insert(0);

    const int MOD = 1'000'000'007;
    while (!djset.empty()) {
      int u = *djset.begin();
      djset.erase(djset.begin());

      auto [udist, uways] = dist_ways[u];
      for (auto [v, w] : adj[u]) {
        if (!dist_ways.count(v)) {
          dist_ways[v] = {udist + w, uways};
          djset.insert(v);
          continue;
        }
        auto& [vdist, vways] = dist_ways[v];
        if (vdist == udist + w) {
          vways += uways;
          if (vways >= MOD) vways -= MOD;
        } else if (vdist > udist + w) {
          djset.erase(v);
          vdist = udist + w;
          vways = uways;
          djset.insert(v);
        }
      }
    }
    return dist_ways[n - 1].second;
  }
};
```
## Tags

* [Graph theory](/README.md#Graph_theory) > [Dijkstra's algorithm](/README.md#Graph_theory-Dijkstra_s_algorithm)
* [Priority queue](/README.md#Priority_queue) > [Key update using insert and remove on C++ set](/README.md#Priority_queue-Key_update_using_insert_and_remove_on_C___set)
