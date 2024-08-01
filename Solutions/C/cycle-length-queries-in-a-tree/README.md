# Cycle length queries in a tree

[Problem link](https://leetcode.com/problems/cycle-length-queries-in-a-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

class Solution {
 public:
  vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) {
    vector<int> ret;
    for (auto q : queries) {
      int u = q[0], v = q[1], cur = 1;
      while (u != v) {
        ++cur;
        if (u < v)
          v >>= 1;
        else
          u >>= 1;
      }
      ret.push_back(cur);
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree)
