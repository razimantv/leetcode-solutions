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

* [Dynamic programming](/README.md#Dynamic_programming)
* [Mathematics](/README.md#Mathematics) > [Reduce problem dimension with proofs](/README.md#Mathematics-Reduce_problem_dimension_with_proofs)
* [Mathematics](/README.md#Mathematics) > [Probability](/README.md#Mathematics-Probability)
