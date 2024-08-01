# Best time to buy and sell stock ii

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution {
 public:
  int maxProfit(vector<int>& prices) {
    int ret = 0, N = prices.size();
    for (int i = 0; i < N; i++) {
      if (i < N - 1 and prices[i] < prices[i + 1]) ret -= prices[i];
      if (i > 0 and prices[i] > prices[i - 1]) ret += prices[i];
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
