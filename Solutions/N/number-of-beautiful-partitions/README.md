# Number of beautiful partitions

[Problem link](https://leetcode.com/problems/number-of-beautiful-partitions/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-beautiful-partitions/

class Solution {
 public:
  void add(int& x, int y) {
    const int MOD = 1'000'000'007;
    x += y;
    if (x >= MOD) x -= MOD;
  }
  int beautifulPartitions(string s, int k, int m) {
    int L = s.size();
    vector<int> p{0, 0, 1, 1, 0, 1, 0, 1, 0, 0};
    if (!p[s[0] - '0'] or p[s[L - 1] - '0']) return 0;

    // dp(i,j) = sum_{ii=0 to i-m+1} dp(ii-1, j-1) if s(ii) is prime
    vector<vector<int>> dp(L + 1, vector<int>(k + 1)), dpsum = dp;
    dp[0][0] = 1;
    for (int i = 0; i < L; ++i) {
      dpsum[i + 1] = dpsum[i];
      if (p[s[i] - '0']) {
        for (int j = 0; j <= k; ++j) add(dpsum[i + 1][j], dp[i][j]);
      } else if (i + 1 >= m) {
        for (int j = 1; j <= k; ++j) dp[i + 1][j] = dpsum[i - m + 2][j - 1];
      }
    }
    return dp[L][k];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
