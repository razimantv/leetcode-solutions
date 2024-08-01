# Restore ip addresses

[Problem link](https://leetcode.com/problems/restore-ip-addresses/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/restore-ip-addresses/

class Solution {
 public:
  vector<string> restoreIpAddresses(string s) {
    int n = s.size();
    using split = vector<string>;
    vector<vector<split>> dp(n + 1, vector<split>(5));
    dp[n][0] = {""};

    for (int i = n - 1; i >= 0; --i) {
      for (int j = i, pref = 0; j < n and pref < 100; ++j) {
        pref = pref * 10 + s[j] - '0';
        if (pref > 255) break;
        string add = to_string(pref);
        if (j == n - 1) dp[i][1] = {add};
        for (int k = 1; k < 4; ++k)
          for (auto next : dp[j + 1][k])
            dp[i][k + 1].push_back(add + "." + next);
        if (!pref) break;
      }
    }
    return dp[0][4];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
