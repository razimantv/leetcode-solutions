# Maximum number of jumps to reach the last index

[Problem link](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

class Solution {
 public:
  int maximumJumps(vector<int>& nums, long long target) {
    int n = nums.size();
    vector<int> dp(n, -1);
    dp[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i)
      for (int j = i + 1; j < n; ++j)
        if (dp[j] >= 0 and nums[j] >= nums[i] - target and
            nums[j] <= nums[i] + target)
          dp[i] = max(dp[i], dp[j] + 1);
    return dp[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
