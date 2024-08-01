# Longest cycle in a graph

[Problem link](https://leetcode.com/problems/longest-cycle-in-a-graph)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-cycle-in-a-graph

class Solution {
 public:
  int longestCycle(vector<int>& edges) {
    int n = edges.size(), ret = -1;
    vector<int> start(n, -1), depth(n);
    for (int i = 0; i < n; ++i) {
      if (start[i] + 1) continue;
      for (int j = i, x = 0; j != -1; j = edges[j], x++) {
        if (start[j] + 1) {
          if (start[j] == i) ret = max(ret, x - depth[j]);
          break;
        }
        depth[j] = x;
        start[j] = i;
      }
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Single outdegree graphs](/Collections/graph-theory.md#single-outdegree-graphs)
