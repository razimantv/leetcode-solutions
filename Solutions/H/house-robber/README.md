# House robber

[Problem link](https://leetcode.com/problems/house-robber)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/house-robber

class Solution {
 public:
  int rob(vector<int>& nums) {
    for (int i = 1, N = nums.size(); i < N; ++i) {
      nums[i] = max(nums[i - 1], nums[i] + ((i > 1) ? nums[i - 2] : 0));
    }
    return nums.empty() ? 0 : nums.back();
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
