# Minimum absolute difference between elements with constraint

[Problem link](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

class Solution {
 public:
  int minAbsoluteDifference(vector<int>& nums, int x) {
    set<int> seen;
    int ret{INT_MAX};
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (i >= x) seen.insert(nums[i - x]);
      int cur = nums[i];
      auto sit = seen.lower_bound(cur);
      if (sit != seen.end()) ret = min(ret, *sit - cur);
      if (sit != seen.begin()) ret = min(ret, cur - *--sit);
    }
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
