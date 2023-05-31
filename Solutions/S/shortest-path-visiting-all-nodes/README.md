# Shortest path visiting all nodes

[Problem link](https://leetcode.com/problems/shortest-path-visiting-all-nodes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-path-visiting-all-nodes

class Solution {
 public:
  int N;
  vector<vector<int>> dist;
  map<pair<int, int>, int> cache;

  int work(int mask, int u) {
    if (!mask) return 0;
    int& best = cache[{mask, u}];
    if (best) return best;

    best = 1 << 20;
    for (int i = 0; i < N; ++i)
      if (mask & (1 << i))
        best = min(best, work(mask ^ (1 << i), i) + dist[i][u]);
    return best;
  }
  int shortestPathLength(vector<vector<int>>& graph) {
    N = graph.size();
    dist = vector<vector<int>>(N, vector<int>(N, -1));

    for (int i = 0; i < N; ++i) {
      queue<int> bfsq;
      bfsq.push(i);
      dist[i][i] = 0;

      while (!bfsq.empty()) {
        int u = bfsq.front();
        bfsq.pop();
        for (int v : graph[u])
          if (dist[i][v] == -1) dist[i][v] = dist[i][u] + 1, bfsq.push(v);
      }
    }
    int best = 1 << 20, fullmask = (1 << N) - 1;
    for (int i = 0; i < N; ++i) best = min(best, work(fullmask ^ (1 << i), i));
    return best;
  }
};
```