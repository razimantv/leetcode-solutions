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

* [Dynamic programming](/README.md#Dynamic_programming) > [Array reuse](/README.md#Dynamic_programming-Array_reuse)
* [Dynamic programming](/README.md#Dynamic_programming) > [Knapsack](/README.md#Dynamic_programming-Knapsack)
