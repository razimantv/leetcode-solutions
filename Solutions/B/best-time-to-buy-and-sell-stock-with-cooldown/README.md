# Best time to buy and sell stock with cooldown

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution {
 public:
  int maxProfit(vector<int>& prices) {
    if (prices.size() < 2) return 0;
    int N = prices.size(), ret = 0;
    vector<int> dp(N + 2, 0), best(N, 0);
    for (int i = 0; i < N; ++i) {
      dp[i + 2] = dp[i + 1];
      if (i > 0) dp[i + 2] = max(dp[i + 2], prices[i] + best[i - 1]);
      best[i] = dp[i] - prices[i];
      if (i > 0) best[i] = max(best[i], best[i - 1]);
    }
    return dp.back();
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
