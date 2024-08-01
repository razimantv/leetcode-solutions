# Queries on number of points inside a circle

[Problem link](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle

class Solution {
 public:
  vector<int> countPoints(vector<vector<int>>& points,
                          vector<vector<int>>& queries) {
    vector<int> ret;
    for (auto& q : queries) {
      int x = q[0], y = q[1], r = q[2];
      int cur = 0;
      for (auto& p : points) {
        int xx = p[0], yy = p[1];
        if ((x - xx) * (x - xx) + (y - yy) * (y - yy) <= r * r) ++cur;
      }
      ret.push_back(cur);
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
