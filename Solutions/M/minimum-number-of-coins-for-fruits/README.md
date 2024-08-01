# Minimum number of coins for fruits

[Problem link](https://leetcode.com/problems/minimum-number-of-coins-for-fruits/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        for i in range(n-1, -1, -1):
            if 2 * i + 3 > n:
                continue
            prices[i] += min(prices[i+1:2*i+3])
        return prices[0]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
