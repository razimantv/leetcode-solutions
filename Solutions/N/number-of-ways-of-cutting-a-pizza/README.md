# Number of ways of cutting a pizza

[Problem link](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

class Solution {
 public:
  int ways(vector<string>& pizza, int k) {
    int m = pizza.size(), n = pizza[0].size();
    vector<vector<int>> psum(m + 1, vector<int>(n + 1));
    vector<vector<long long>> dp(m, vector<long long>(n));
    for (int i = m - 1; i >= 0; --i)
      for (int j = n - 1; j >= 0; --j) {
        psum[i][j] = (pizza[i][j] == 'A') + psum[i + 1][j] + psum[i][j + 1] -
                     psum[i + 1][j + 1];
        dp[i][j] = (psum[i][j] > 0);
      }

    while (--k)
      for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j) {
          dp[i][j] = 0;
          for (int ip = i + 1; ip < m; ++ip)
            if (psum[i][j] > psum[ip][j]) dp[i][j] += dp[ip][j];
          for (int jp = j + 1; jp < n; ++jp)
            if (psum[i][j] > psum[i][jp]) dp[i][j] += dp[i][jp];
          dp[i][j] %= 1'000'000'007;
        }
    return dp[0][0];
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [2D](/Collections/prefix.md#2d)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
