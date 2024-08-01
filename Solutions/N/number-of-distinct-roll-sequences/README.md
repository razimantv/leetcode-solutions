# Number of distinct roll sequences

[Problem link](https://leetcode.com/problems/number-of-distinct-roll-sequences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-distinct-roll-sequences

class Solution {
 public:
  int distinctSequences(int n) {
    if (n == 1)
      return 6;
    else if (n == 2)
      return 22;
    vector<vector<vector<int>>> dp(n + 1,
                                   vector<vector<int>>(6, vector<int>(6)));
    for (int i = 0; i < 6; ++i)
      for (int j = 0; j < 6; ++j)
        if (__gcd(i + 1, j + 1) == 1 and j != i) dp[2][i][j] = 1;

    const int MOD = 1'000'000'007;
    for (int i = 3; i <= n; ++i)
      for (int j = 0; j < 6; ++j)
        for (int k = 0; k < 6; ++k) {
          if (!dp[2][j][k]) continue;
          for (int l = 0; l < 6; ++l) {
            if (l != k) {
              dp[i][j][k] += dp[i - 1][l][j];
              if (dp[i][j][k] >= MOD) dp[i][j][k] -= MOD;
            }
          }
        }

    int ret{};
    for (auto& v : dp.back())
      for (int x : v) {
        ret += x;
        if (ret >= MOD) ret -= MOD;
      }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
