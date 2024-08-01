# Falling squares

[Problem link](https://leetcode.com/problems/falling-squares)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/falling-squares

class Solution {
 public:
  vector<int> fallingSquares(vector<vector<int>>& positions) {
    map<int, int> cc;
    for (auto& xl : positions) {
      cc[xl[0]] = cc[xl[0] + xl[1]] = 0;
    }

    int best = 0;
    vector<int> ret;
    for (auto& rec : positions) {
      int xl = rec[0], xr = xl + rec[1];
      auto s = cc.find(xl);

      int cur = 0;
      for (auto mit = s; mit->first < xr; ++mit) cur = max(cur, mit->second);
      cur += rec[1];
      for (auto mit = s; mit->first < xr; ++mit) mit->second = cur;

      best = max(best, cur);
      ret.push_back(best);
    }
    return ret;
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Non-overlapping decomposition](/Collections/intervals.md#non-overlapping-decomposition)
