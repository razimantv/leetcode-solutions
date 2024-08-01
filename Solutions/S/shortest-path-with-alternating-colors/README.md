# Shortest path with alternating colors

[Problem link](https://leetcode.com/problems/shortest-path-with-alternating-colors/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution {
 public:
  vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges,
                                       vector<vector<int>>& blueEdges) {
    vector<vector<vector<int>>> adj(2, vector<vector<int>>(n));
    for (int x : {0, 1}) {
      auto& edges = x ? redEdges : blueEdges;
      for (auto& e : edges) adj[x][e[0]].push_back(e[1]);
    }
    queue<pair<int, int>> bfsq;
    vector<int> ret(n, -1);
    vector<vector<int>> dist(2, vector<int>(n, -1));
    ret[0] = dist[0][0] = dist[1][0] = 0;
    bfsq.push({0, 0});
    bfsq.push({0, 1});

    while (!bfsq.empty()) {
      auto [u, x] = bfsq.front();
      int y = 1 - x;
      bfsq.pop();
      for (int v : adj[x][u]) {
        if (dist[y][v] == -1) {
          dist[y][v] = dist[x][u] + 1;
          bfsq.push({v, y});
          if (ret[v] == -1) ret[v] = dist[y][v];
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Multi source search](/Collections/graph-theory.md#multi-source-search)
