# Restore the array

[Problem link](https://leetcode.com/problems/restore-the-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/restore-the-array/

class Solution {
 public:
  int numberOfArrays(string s, int k) {
    int n = s.size();
    const int MOD{1'000'000'007};
    vector<int> dp(n + 1);
    dp[n] = 1;
    for (int i = n - 1; i >= 0; --i) {
      if (s[i] == '0') continue;
      int& x = dp[i];
      for (auto [j, pref] = make_pair(i, 0ll); j < n; ++j) {
        pref = pref * 10 + s[j] - '0';
        if (pref > k) break;
        x += dp[j + 1];
        if (x >= MOD) x -= MOD;
      }
    }
    return dp[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
