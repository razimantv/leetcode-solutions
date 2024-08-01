# Minimize maximum of array

[Problem link](https://leetcode.com/problems/minimize-maximum-of-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-maximum-of-array/

class Solution {
 public:
  int minimizeArrayValue(vector<int>& nums) {
    reverse(nums.begin(), nums.end());
    long long m = *min_element(nums.begin(), nums.end()) - 1,
              M = *max_element(nums.begin(), nums.end());
    while (M - m > 1) {
      long long mid = (M + m) >> 1, cur = 0;
      for (int x : nums) {
        if (x > mid)
          cur += x - mid;
        else
          cur = max(0ll, cur - (mid - x));
      }
      (cur ? m : M) = mid;
    }
    return M;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
