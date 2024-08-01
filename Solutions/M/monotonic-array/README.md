# Monotonic array

[Problem link](https://leetcode.com/problems/monotonic-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/monotonic-array/

class Solution {
 public:
  bool isMonotonic(vector<int>& nums) {
    for (int i = 1, n = nums.size(), inc{}, dec{}; i < n; ++i) {
      if (nums[i] > nums[i - 1])
        inc = 1;
      else if (nums[i] < nums[i - 1])
        dec = 1;
      if (inc && dec) return false;
    }
    return true;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
