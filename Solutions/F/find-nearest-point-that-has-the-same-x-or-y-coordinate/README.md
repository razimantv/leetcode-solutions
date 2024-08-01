# Find nearest point that has the same x or y coordinate

[Problem link](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate

class Solution {
 public:
  int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
    int best = 1000000, besti = -1;
    for (int i = -1; const auto& v : points) {
      ++i;
      int xx = v[0], yy = v[1];
      if (xx != x and yy != y) continue;
      int cur = abs(x - xx) + abs(y - yy);
      if (cur < best) best = cur, besti = i;
    }
    return besti;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
