# Tallest billboard

[Problem link](https://leetcode.com/problems/tallest-billboard/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/tallest-billboard/

class Solution {
 public:
  int tallestBillboard(vector<int>& rods) {
    int smax = accumulate(rods.begin(), rods.end(), 0) / 2;
    unordered_map<int, int> dp{{0, 0}};
    for (int x : rods) {
      auto next = dp;
      for (auto [k, v] : dp) {
        int knext = k + x;
        if (knext <= smax) next[knext] = max(next[knext], v);
        knext = abs(k - x);
        if (knext <= smax) next[knext] = max(next[knext], v + min(x, k));
      }
      dp = next;
    }
    return dp[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Partial bottom-up](/Collections/dynamic-programming.md#partial-bottom-up)
