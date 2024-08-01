# Maximum score from performing multiplication operations

[Problem link](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations

class Solution {
 public:
  int maximumScore(vector<int>& nums, vector<int>& multipliers) {
    int n = nums.size(), m = multipliers.size();

    // dp(i, j) = maximum score after i operations
    //            if j elements have been taken from left side
    // Reuse dp array to reduce dimension
    vector<int> dp(m + 1);
    for (int i = 1; i <= m; ++i) {
      // dp(i, j) = max(dp(i-1,j-1) + mult(i)*nums(j),
      //                dp(i-1, j ) + mult(i)*nums(n-j))
      // With index changes to deal with 0-based arrays
      int mult = multipliers[i - 1];
      dp[i] = dp[i - 1] + mult * nums[i - 1];
      for (int j = i - 1; j; --j) {
        dp[j] =
            max(dp[j - 1] + mult * nums[j - 1], dp[j] + mult * nums[n - i + j]);
      }
      dp[0] += mult * nums[n - i];
    }
    return *max_element(dp.begin(), dp.end());
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
