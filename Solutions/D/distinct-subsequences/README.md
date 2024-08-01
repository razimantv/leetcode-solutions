# Distinct subsequences

[Problem link](https://leetcode.com/problems/distinct-subsequences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distinct-subsequences

class Solution {
 public:
  int numDistinct(string s, string t) {
    int L = t.size();
    vector<long long> DP(L + 1);
    DP[0] = 1;
    for (char c : s)
      for (int i = L - 1; i >= 0; --i)
        if (c == t[i]) DP[i + 1] = (DP[i + 1] + DP[i]) & ((1ll << 32) - 1);
    return DP[L];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
