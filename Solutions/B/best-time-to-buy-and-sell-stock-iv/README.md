# Best time to buy and sell stock iv

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution {
 public:
  int maxProfit(int k, vector<int>& prices) {
    if (prices.empty()) return 0;

    int N = prices.size();
    k = min(k, N / 2);

    vector<int> best0(k + 1, 0), best1(k + 1, -1e9);
    for (int p : prices) {
      for (int j = k; j > 0; --j) {
        best0[j] = max(best0[j], best1[j] + p);
        best1[j] = max(best1[j], best0[j - 1] - p);
      }
    }

    return *max_element(best0.begin(), best0.end());
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
