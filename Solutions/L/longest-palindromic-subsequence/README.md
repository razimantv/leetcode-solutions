# Longest palindromic subsequence

[Problem link](https://leetcode.com/problems/longest-palindromic-subsequence/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
 public:
  int longestPalindromeSubseq(string s) {
    int n = s.size();
    vector<int> dp2(n), dp1(n, 1);
    for (int l = 2; l <= n; ++l) {
      vector<int> dp(n - l + 1);
      for (int i = 0, j = i + l - 1; j < n; ++i, ++j)
        dp[i] = (s[i] == s[j]) ? (dp2[i + 1] + 2) : max(dp1[i], dp1[i + 1]);
      dp2 = dp1;
      dp1 = dp;
    }
    return dp1[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
