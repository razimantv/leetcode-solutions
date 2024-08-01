# Minimum cost of a path with special roads

[Problem link](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

class Solution {
 public:
  int minimumCost(vector<int>& start, vector<int>& end,
                  vector<vector<int>>& roads) {
    roads.push_back({start[0], start[1], end[0], end[1],
                     abs(start[0] - end[0]) + abs(start[1] - end[1])});
    int n = roads.size();
    vector<int> dist(2 * n, 1'000'000);
    auto cmp = [&](int i, int j) {
      if (dist[i] != dist[j]) return dist[i] < dist[j];
      return i < j;
    };
    set<int, decltype(cmp)> djset(cmp);
    auto update = [&](int u, int val) {
      if (dist[u] <= val) return;
      if (djset.count(u)) djset.erase(u);
      dist[u] = val;
      djset.insert(u);
    };
    for (int i = 0; i < n; ++i)
      update(2 * i, abs(start[0] - roads[i][0]) + abs(start[1] - roads[i][1]));

    while (!djset.empty()) {
      int u = *djset.begin();
      djset.erase(djset.begin());
      if (u == 2 * n - 1) break;

      int i = u >> 1;
      if (u & 1) {
        for (int j = 0; j < n; ++j)
          update(j << 1, dist[u] + abs(roads[i][2] - roads[j][0]) +
                             abs(roads[i][3] - roads[j][1]));
        update(2 * n - 1,
               dist[u] + abs(roads[i][2] - end[0]) + abs(roads[i][3] - end[1]));
      } else {
        update(u ^ 1, dist[u] + roads[i][4]);
      }
    }
    return dist.back();
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Dijkstra's algorithm](/Collections/priority-queue.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
