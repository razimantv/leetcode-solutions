# Find closest node to given two nodes

[Problem link](https://leetcode.com/problems/find-closest-node-to-given-two-nodes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes

class Solution {
 public:
  int closestMeetingNode(vector<int>& edges, int n1, int n2) {
    unordered_map<int, int> d1, d2;
    int x = 0;
    while (n1 != -1 and !d1.count(n1)) d1[n1] = x++, n1 = edges[n1];
    x = 0;
    while (n2 != -1 and !d2.count(n2)) d2[n2] = x++, n2 = edges[n2];

    int ret = -1, best = INT_MAX;
    for (int i = 0, n = edges.size(); i < n; ++i)
      if (d1.count(i) and d2.count(i)) {
        int cur = max(d1[i], d2[i]);
        if (cur < best) best = cur, ret = i;
      }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Single outdegree graphs](/Collections/graph-theory.md#single-outdegree-graphs)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Cycle detection](/Collections/graph-theory.md#cycle-detection)
