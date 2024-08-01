# Longest even odd subarray with threshold

[Problem link](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution {
 public:
  int longestAlternatingSubarray(vector<int>& nums, int threshold) {
    int ret{0};
    for (int i = 0, n = nums.size(), start = -1; i < n; ++i) {
      if (nums[i] > threshold)
        start = -1;
      else if (start != -1) {
        if ((nums[i] ^ nums[i - 1]) & 1)
          ret = max(ret, i - start + 1);
        else if (!(nums[i] & 1))
          start = i;
        else
          start = -1;
      } else if (!(nums[i] & 1)) {
        ret = max(ret, 1);
        start = i;
      }
    }
    return ret;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
