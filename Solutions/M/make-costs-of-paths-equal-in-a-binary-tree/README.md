# Make costs of paths equal in a binary tree

[Problem link](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
 public:
  int minIncrements(int n, vector<int>& cost) {
    int ret{};
    for (int rc = n - 1, lc = rc - 1, node = lc >> 1; node >= 0;
         --node, lc -= 2, rc -= 2) {
      ret += max(cost[lc], cost[rc]) - min(cost[lc], cost[rc]);
      cost[node] += max(cost[lc], cost[rc]);
    }
    return ret;
  }
};
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Iteration](/Collections/tree.md#iteration)
* [Greedy](/Collections/greedy.md#greedy)
