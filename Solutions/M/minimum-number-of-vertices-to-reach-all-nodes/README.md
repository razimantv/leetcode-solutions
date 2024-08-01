# Minimum number of vertices to reach all nodes

[Problem link](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution {
 public:
  vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
    unordered_set<int> s;
    for (auto e : edges) s.insert(e[1]);
    vector<int> ret;
    for (int i = 0; i < n; ++i)
      if (!s.count(i)) ret.push_back(i);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
