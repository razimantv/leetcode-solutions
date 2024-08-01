# All paths from source to target

[Problem link](https://leetcode.com/problems/all-paths-from-source-to-target)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution {
  vector<vector<int>> ret;
  vector<int> prefix;

 public:
  vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph,
                                           int start = 0) {
    prefix.push_back(start);
    if (start + 1 == graph.size()) {
      ret.push_back(prefix);
    } else {
      for (int u : graph[start]) allPathsSourceTarget(graph, u);
    }
    prefix.pop_back();
    return start ? vector<vector<int>>() : ret;
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
