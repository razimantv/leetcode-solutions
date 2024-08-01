# Determine if a cell is reachable at a given time

[Problem link](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution {
 public:
  bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
    if (sx == fx and sy == fy and t == 1) return false;
    long long dx = abs(sx - fx), dy = abs(sy - fy);
    return max(dx, dy) <= t;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
