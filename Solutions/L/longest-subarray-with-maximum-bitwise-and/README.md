# Longest subarray with maximum bitwise and

[Problem link](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution {
 public:
  int longestSubarray(vector<int>& nums) {
    int best = 1, val = nums[0], n = nums.size();
    for (int i = 1, start = 0; i < n; ++i) {
      if (nums[i] != nums[start]) start = i;
      if (nums[i] > val) val = nums[i], best = 1;
      if (nums[i] == val) best = max(best, i - start + 1);
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
