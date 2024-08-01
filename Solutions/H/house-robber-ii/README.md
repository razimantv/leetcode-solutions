# House robber ii

[Problem link](https://leetcode.com/problems/house-robber-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/house-robber-ii

class Solution {
 public:
  int rob(const vector<int>& nums, int l, int r) {
    int a = max(nums[l], nums[l + 1]), b = nums[l], best = a;
    for (int i = l + 2; i < r; ++i) {
      int temp = a;
      a = b + nums[i];
      b = max(b, temp);
    }
    return max(a, b);
  }
  int rob(vector<int>& nums) {
    int N = nums.size();
    if (N == 1)
      return nums[0];
    else if (N == 2)
      return max(nums[0], nums[1]);
    return max(rob(nums, 0, N - 1), rob(nums, 1, N));
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Cyclic array](/Collections/dynamic-programming.md#cyclic-array)
