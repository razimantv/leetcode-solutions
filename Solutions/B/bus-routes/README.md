# Bus routes

[Problem link](https://leetcode.com/problems/bus-routes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/bus-routes

class Solution {
 public:
  int numBusesToDestination(vector<vector<int>>& routes, int source,
                            int target) {
    vector<vector<int>> adj(123456);
    for (int i = 0; i < routes.size(); ++i) {
      for (int s : routes[i]) {
        adj[s].push_back(100001 + i);
        adj[100001 + i].push_back(s);
      }
    }

    vector<int> dist(123456);
    dist[source] = 1;
    queue<int> bfsq;
    bfsq.push(source);
    while (!bfsq.empty()) {
      int u = bfsq.front();
      bfsq.pop();
      if (u == target) return dist[u] / 2;

      for (int v : adj[u]) {
        if (!dist[v]) {
          dist[v] = dist[u] + 1;
          bfsq.push(v);
        }
      }
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
