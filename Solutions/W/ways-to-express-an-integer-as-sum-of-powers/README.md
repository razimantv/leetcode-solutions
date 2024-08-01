# Ways to express an integer as sum of powers

[Problem link](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution {
 public:
  int numberOfWays(int n, int x) {
    int large = ceil(pow(n, 1. / x));
    vector<int> xpow;
    for (int i = 0; i <= large; ++i) {
      xpow.push_back(1);
      for (int j = 0; j < x; ++j) xpow.back() *= i;
    }

    const int MOD = 1'000'000'007;
    vector<vector<int>> dp(n + 1, vector<int>(large + 1));
    dp[0][0] = 1;
    for (int i = 0; i <= n; ++i)
      for (int j = 1; j <= large; ++j) {
        dp[i][j] = dp[i][j - 1] + (xpow[j] <= i ? dp[i - xpow[j]][j - 1] : 0);
        if (dp[i][j] >= MOD) dp[i][j] -= MOD;
      }
    return dp[n][large];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
