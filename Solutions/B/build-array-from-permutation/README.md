# Build array from permutation

[Problem link](https://leetcode.com/problems/build-array-from-permutation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/build-array-from-permutation

class Solution {
 public:
  vector<int> buildArray(vector<int>& nums) {
    vector<int> ret(nums.size());
    for (int i = 0, n = nums.size(); i < n; ++i) ret[i] = nums[nums[i]];
    return ret;
  }
};
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [Inverse](/Collections/permutation.md#inverse)
