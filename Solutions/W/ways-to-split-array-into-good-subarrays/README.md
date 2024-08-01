# Ways to split array into good subarrays

[Problem link](https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution {
 public:
  int numberOfGoodSubarraySplits(vector<int>& nums) {
    long long ret{1};
    bool seen{};
    for (int i = 0, n = nums.size(), prev = -1; i < n; ++i) {
      if (nums[i]) {
        if (prev != -1) ret = (ret * (i - prev)) % 1'000'000'007;
        prev = i;
        seen = 1;
      }
    }
    return ret * seen;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
