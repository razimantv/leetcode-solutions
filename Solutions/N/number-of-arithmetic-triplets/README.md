# Number of arithmetic triplets

[Problem link](https://leetcode.com/problems/number-of-arithmetic-triplets)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution {
 public:
  int arithmeticTriplets(vector<int>& nums, int diff) {
    int n = nums.size(), ret{};
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < i; ++j)
        for (int k = 0; k < j; ++k)
          if (nums[i] - nums[j] == diff and nums[j] - nums[k] == diff) ++ret;
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
