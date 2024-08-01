# Minimum height trees

[Problem link](https://leetcode.com/problems/minimum-height-trees)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-height-trees

class Solution {
  vector<int> parent, dist;
  vector<vector<int>> adjlist;
  int best, bestval;
  void dfs(int u, int par = -1, int d = 0) {
    parent[u] = par;
    if (bestval < (dist[u] = d)) {
      bestval = d;
      best = u;
    }

    for (int v : adjlist[u]) {
      if (v == par) continue;
      dfs(v, u, d + 1);
    }
  }

 public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    adjlist.resize(n);
    parent.resize(n);
    dist.resize(n);
    for (const auto& e : edges) {
      adjlist[e[0]].push_back(e[1]);
      adjlist[e[1]].push_back(e[0]);
    }

    best = bestval = 0;
    dfs(0);
    bestval = 0;
    dfs(best);

    vector<int> ret;
    for (int i = 0, jump = (bestval >> 1); i < jump; ++i) best = parent[best];
    ret.push_back(best);
    if (bestval & 1) ret.push_back(parent[best]);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Tree diameter](/Collections/graph-theory.md#tree-diameter)
