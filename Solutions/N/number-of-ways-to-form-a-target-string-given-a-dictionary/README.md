# Number of ways to form a target string given a dictionary

[Problem link](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution {
 public:
  int numWays(vector<string>& words, string target) {
    int Lw = words[0].size(), Lt = target.size();
    vector<int> dp(Lt + 1);
    dp.back() = 1;
    for (int i = Lw - 1; i >= 0; --i) {
      vector<int> cnt(26);
      for (const auto& word : words) ++cnt[word[i] - 'a'];
      for (int j = max(0, Lt - Lw + i); j < Lt; ++j)
        dp[j] =
            (dp[j] + cnt[target[j] - 'a'] * 1ll * dp[j + 1]) % 1'000'000'007;
    }
    return dp[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
