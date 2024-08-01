# Check if all 1s are at least length k places away

[Problem link](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away

class Solution {
 public:
  bool kLengthApart(vector<int>& nums, int k) {
    int prev = -k - 1;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (nums[i] == 1)
        if (i - prev <= k)
          return false;
        else
          prev = i;
    }
    return true;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
