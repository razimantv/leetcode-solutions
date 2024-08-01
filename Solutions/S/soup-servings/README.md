# Soup servings

[Problem link](https://leetcode.com/problems/soup-servings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/soup-servings/

class Solution {
 public:
  double soupServings(int n) {
    if (!n)
      return .5;
    else if (n > 5000)
      return 1.;

    n = (n + 24) / 25;
    vector<vector<double>> dp(n + 1, vector<double>(n + 1));
    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= n; ++j)
        for (int di = 4, dj = 0; di; --di, ++dj) {
          int ii = i - di, jj = j - dj;
          if (ii <= 0 and jj <= 0)
            dp[i][j] += 1. / 8;
          else if (ii <= 0)
            dp[i][j] += 1. / 4;
          else if (jj > 0)
            dp[i][j] += dp[ii][jj] / 4;
        }
    return dp[n][n];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Reduce problem dimension with proofs](/Collections/mathematics.md#reduce-problem-dimension-with-proofs)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
