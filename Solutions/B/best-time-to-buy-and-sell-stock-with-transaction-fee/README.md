# Best time to buy and sell stock with transaction fee

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution {
 public:
  int maxProfit(vector<int>& prices, int fee) {
    int bestwithout = 0, bestwith = -2'000'000'000;
    for (int p : prices) {
      int newbest = max(bestwithout, bestwith + p);
      bestwith = max(bestwith, bestwithout - p - fee);
      bestwithout = newbest;
    }
    return bestwithout;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
