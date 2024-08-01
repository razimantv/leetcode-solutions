# Longest subarray of 1s after deleting one element

[Problem link](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution {
 public:
  int longestSubarray(vector<int>& nums) {
    int best{};
    for (int l = 0, r = 0, n = nums.size(), bad = 0; r < n; ++r) {
      if (!nums[r]) ++bad;
      while (bad > 1)
        if (!nums[l++]) --bad;
      best = max(best, r - l);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
