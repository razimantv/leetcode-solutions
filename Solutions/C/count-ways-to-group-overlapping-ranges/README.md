# Count ways to group overlapping ranges

[Problem link](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution {
 public:
  int countWays(vector<vector<int>>& ranges) {
    sort(ranges.begin(), ranges.end());
    int last = ranges[0][0] - 1, ret = 1, MOD = 1'000'000'007;
    for (auto r : ranges) {
      if (r[0] > last) {
        ret <<= 1;
        if (ret >= MOD) ret -= MOD;
      }
      last = max(last, r[1]);
    }
    return ret;
  }
};
```
## Tags

* [Intervals](/README.md#Intervals) > [Overlap](/README.md#Intervals-Overlap)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
