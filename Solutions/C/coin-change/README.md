# Coin change

[Problem link](https://leetcode.com/problems/coin-change)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/coin-change

class Solution {
 public:
  int coinChange(vector<int>& coins, int amount) {
    vector<int> result(amount + 1, amount + 1);
    result[0] = 0;
    for (int c : coins) {
      for (int i = c; i <= amount; ++i) {
        result[i] = min(result[i], result[i - c] + 1);
      }
    }
    if (result[amount] > amount)
      return -1;
    else
      return result[amount];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
