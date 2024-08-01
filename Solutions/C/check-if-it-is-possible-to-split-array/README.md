# Check if it is possible to split array

[Problem link](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution {
 public:
  bool canSplitArray(vector<int>& nums, int m) {
    int n = nums.size();
    vector<vector<int>> dp(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
      dp[i][i] = 1;
      if (i) {
        nums[i] += nums[i - 1];
        dp[i - 1][i] = 1;
      }
    }

    for (int l = 2; l < n; ++l)
      for (int i = 0, j = i + l; j < n; ++i, ++j)
        for (int k = i; k < j; ++k) {
          if (dp[i][k] and dp[k + 1][j] and
              (k == i or (nums[k] - (i ? nums[i - 1] : 0) >= m)) and
              (k + 1 == j or nums[j] - nums[k] >= m)) {
            dp[i][j] = 1;
            break;
          }
        }
    return dp[0][n - 1];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
