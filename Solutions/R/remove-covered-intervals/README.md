# Remove covered intervals

[Problem link](https://leetcode.com/problems/remove-covered-intervals)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-covered-intervals

class Solution {
 public:
  int removeCoveredIntervals(vector<vector<int>>& I) {
    int cnt{0};
    for (int i = 0; i < I.size(); ++i) {
      bool flag{true};
      for (int j = 0; j < I.size(); ++j) {
        if (j == i) continue;
        if (I[j][0] <= I[i][0] and I[j][1] >= I[i][1]) {
          flag = false;
          break;
        }
      }
      if (flag) ++cnt;
    }
    return cnt;
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Overlap](/Collections/intervals.md#overlap)
