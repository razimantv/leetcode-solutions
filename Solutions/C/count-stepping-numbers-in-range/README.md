# Count stepping numbers in range

[Problem link](https://leetcode.com/problems/count-stepping-numbers-in-range/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-stepping-numbers-in-range/

class Solution {
 public:
  const int MOD = 1'000'000'007;
  void inc(int& x, int y) {
    if ((x += y) >= MOD) x -= MOD;
  }

  int countSteppingNumbers(string low, string high) {
    int N = high.size();

    vector<vector<int>> dp(N + 1, vector<int>(10));
    vector<int> all(N + 1), alltot(N + 1);
    dp[0] = dp[1] = vector<int>(10, 1);
    all[1] = alltot[1] = 9;
    for (int i = 2; i <= N; ++i) {
      for (int j = 0; j < 10; ++j) {
        dp[i][j] = (j ? dp[i - 1][j - 1] : 0);
        inc(dp[i][j], (j < 9 ? dp[i - 1][j + 1] : 0));
        if (j) inc(all[i], dp[i][j]);
      }
      alltot[i] = alltot[i - 1];
      inc(alltot[i], all[i]);
    }

    auto work = [&](string& lim, bool sub) {
      int n = lim.size();
      if (n == 1) return lim[0] - '0' - sub;

      int ret = alltot[n - 1];
      for (char c = '1'; c < lim[0]; ++c) inc(ret, dp[n][c - '0']);
      for (int i = 1; i < n; ++i) {
        for (char cc = lim[i - 1] - 1; cc <= lim[i - 1] + 1; cc += 2)
          if (cc >= '0' and cc < lim[i]) inc(ret, dp[n - i][cc - '0']);
        if (abs(lim[i] - lim[i - 1]) != 1) break;
        if (i == n - 1 and !sub) inc(ret, 1);
      }
      return ret;
    };

    int ret = work(high, false);
    inc(ret, MOD - work(low, true));
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
