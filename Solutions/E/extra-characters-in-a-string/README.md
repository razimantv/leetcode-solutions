# Extra characters in a string

[Problem link](https://leetcode.com/problems/extra-characters-in-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/extra-characters-in-a-string/

class Solution {
 public:
  int minExtraChar(string s, vector<string>& dictionary) {
    unordered_set<string> good;
    for (auto w : dictionary) good.insert(w);

    int n = s.size();
    vector<int> dp(n + 1);
    for (int i = n - 1; i >= 0; --i) {
      string t;
      dp[i] = 1 + dp[i + 1];
      for (int j = i; j < n; ++j) {
        t += s[j];
        if (good.count(t)) dp[i] = min(dp[i], dp[j + 1]);
      }
    }
    return dp[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Hashmap](/Collections/hashmap.md#hashmap)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
