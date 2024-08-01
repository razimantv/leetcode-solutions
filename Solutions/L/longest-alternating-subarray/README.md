# Longest alternating subarray

[Problem link](https://leetcode.com/problems/longest-alternating-subarray/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
 public:
  int alternatingSubarray(vector<int>& nums) {
    int best{-1};
    for (int i = 1, start = 0, n = nums.size(); i < n; ++i) {
      if ((start ^ i) & 1) {
        if (nums[i] == nums[start] + 1)
          best = max(best, i - start + 1);
        else
          start = i;
      } else {
        if (nums[i] == nums[start])
          best = max(best, i - start + 1);
        else if (nums[i] == nums[i - 1] + 1)
          best = max(best, i - (start = i - 1) + 1);
        else
          start = i;
      }
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
