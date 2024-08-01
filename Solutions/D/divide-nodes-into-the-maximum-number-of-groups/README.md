# Divide nodes into the maximum number of groups

[Problem link](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class Solution {
 public:
  vector<vector<int>> adj;
  vector<int> seen, depth;
  int next;

  void component(int u, vector<int>& comp) {
    comp.push_back(u);
    seen[u] = next;
    for (int v : adj[u])
      if (!seen[v]) component(v, comp);
  }

  int work(const vector<int>& comp) {
    int best = 1;
    for (int start : comp) {
      seen[start] = ++next;
      queue<int> bfsq;
      bfsq.push(start);
      depth[start] = 1;
      while (!bfsq.empty()) {
        int u = bfsq.front();
        bfsq.pop();
        for (int v : adj[u]) {
          if (seen[v] == next) {
            if (depth[v] == depth[u]) return -1;
            continue;
          }
          best = max(best, depth[v] = depth[u] + 1);
          seen[v] = next;
          bfsq.push(v);
        }
      }
    }
    return best;
  }
  int magnificentSets(int n, vector<vector<int>>& edges) {
    adj.resize(n);
    seen.resize(n);
    depth.resize(n);
    next = 0;

    for (auto e : edges) {
      adj[--e[0]].push_back(--e[1]);
      adj[e[1]].push_back(e[0]);
    }

    int ret{};
    for (int i = 0; i < n; ++i) {
      if (seen[i]) continue;
      ++next;
      vector<int> comp;
      component(i, comp);
      int cur = work(comp);
      if (cur == -1) return -1;
      ret += cur;
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Bipartite graph](/Collections/graph-theory.md#bipartite-graph)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Reuse visited array](/Collections/graph-theory.md#reuse-visited-array)
