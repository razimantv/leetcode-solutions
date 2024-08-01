# Count pairs whose sum is less than target

[Problem link](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution {
 public:
  int countPairs(vector<int>& nums, int target) {
    int ret{};
    for (int i = 0, n = nums.size(); i < n; ++i)
      for (int j = 0; j < i; ++j)
        if (nums[i] + nums[j] < target) ++ret;
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
