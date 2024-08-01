# Sorting three groups

[Problem link](https://leetcode.com/problems/sorting-three-groups/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sorting-three-groups/

class Solution {
 public:
  int minimumOperations(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> dp(n + 1, vector<int>(3, n));
    dp[0] = {0, 0, 0};
    for (int i = 0; i < n; ++i) {
      --nums[i];
      for (int j = 0; j < 3; ++j) {
        if (j) dp[i + 1][j] = dp[i + 1][j - 1];
        for (int k = 0; k <= j; ++k)
          dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + (k != nums[i]));
      }
    }
    return *min_element(dp[n].begin(), dp[n].end());
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
