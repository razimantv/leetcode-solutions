# Longest ideal subsequence

[Problem link](https://leetcode.com/problems/longest-ideal-subsequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-ideal-subsequence

class Solution {
 public:
  int longestIdealString(string s, int k) {
    vector<int> best(26);
    for (char c : s) {
      int d = c - 'a', bestprev = 0;
      for (int start = max(d - k, 0), end = min(d + k, 25), i = start; i <= end;
           ++i)
        bestprev = max(bestprev, best[i]);
      best[d] = bestprev + 1;
    }
    return *max_element(best.begin(), best.end());
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
