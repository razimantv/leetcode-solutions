# Best time to buy and sell stock

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution {
 public:
  int maxProfit(vector<int>& prices) {
    int best = 0, m = prices.empty() ? 0 : prices[0];
    for (int p : prices) best = max(best, p - m), m = min(p, m);
    return best;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
