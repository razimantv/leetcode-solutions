# Apply operations to an array

[Problem link](https://leetcode.com/problems/apply-operations-to-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/apply-operations-to-an-array/

class Solution {
 public:
  vector<int> applyOperations(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n - 1; ++i)
      if (nums[i] == nums[i + 1]) nums[i] *= 2, nums[i + 1] = 0;

    vector<int> ret;
    for (int x : nums)
      if (x) ret.push_back(x);
    ret.resize(n);

    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
