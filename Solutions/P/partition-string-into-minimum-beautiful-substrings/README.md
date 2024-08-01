# Partition string into minimum beautiful substrings

[Problem link](https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution {
 public:
  int minimumBeautifulSubstrings(string s) {
    int n = s.size();
    vector<int> dp(n + 1, -2);
    dp.back() = 0;
    unordered_set<int> pow5{1, 5, 25, 125, 625, 3125, 15625};
    function<int(int)> rec = [&](int i) {
      if (dp[i] != -2) return dp[i];
      if (s[i] == '0') return dp[i] = -1;
      dp[i] = 20;
      for (int j = i, pref = 0; j < n; ++j) {
        pref = pref * 2 + s[j] - '0';
        if (pow5.count(pref) and rec(j + 1) != -1)
          dp[i] = min(dp[i], rec(j + 1) + 1);
      }
      if (dp[i] == 20) dp[i] = -1;
      return dp[i];
    };
    return rec(0);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
