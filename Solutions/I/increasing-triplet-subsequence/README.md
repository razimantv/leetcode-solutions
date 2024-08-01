# Increasing triplet subsequence

[Problem link](https://leetcode.com/problems/increasing-triplet-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution {
 public:
  bool increasingTriplet(vector<int>& nums) {
    for (int i = 0, n = nums.size(), s = INT_MAX, s2 = s; i < n; ++i) {
      if (s2 < nums[i]) {
        return true;
      } else if (s < nums[i]) {
        s2 = nums[i];
      } else
        s = nums[i];
    }
    return false;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
