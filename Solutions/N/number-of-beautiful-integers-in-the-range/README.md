# Number of beautiful integers in the range

[Problem link](https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

class Solution {
 public:
  int dp1(int l, int k, string limit) {
    // dp[i][j][r] = number of ways to fill first i digits
    //               such that j of them are odd
    //               and the prefix leaves remainder r mod k
    // If limit is a string, ensure that the prefix stays below
    vector<vector<vector<int>>> dp(l + 1,
                                   vector<vector<int>>(l + 1, vector<int>(k)));
    int prefodd = 0, prefrem = 0;
    dp[0][0][0] = limit.empty();
    for (int i = 0; i < l; ++i) {
      for (int j = 0; j <= i; ++j)
        for (int r = 0; r < k; ++r)
          for (int d = 0 + (i == 0); d < 10; ++d)
            dp[i + 1][j + (d & 1)][(r * 10 + d) % k] += dp[i][j][r];
      if (!limit.empty()) {
        for (int d = 0 + (i == 0); d < limit[i] - '0' + !limit[i + 1]; ++d)
          dp[i + 1][prefodd + (d & 1)][(prefrem * 10 + d) % k]++;
        prefodd += (limit[i] - '0') & 1;
        prefrem = (prefrem * 10 + limit[i] - '0') % k;
      }
    }
    return dp[l][l >> 1][0];
  }

  int work(int n, int k) {
    string sn = to_string(n);
    int L = sn.size(), ret{};
    for (int l = 2; l <= L; l += 2) ret += dp1(l, k, l == L ? sn : "");
    return ret;
  }

  int numberOfBeautifulIntegers(int low, int high, int k) {
    return work(high, k) - work(low - 1, k);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
