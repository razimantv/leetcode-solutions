# Minimum number of coins to be added

[Problem link](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins = sorted(coins)
        lim, ret, c, n = 0, 0, 0, len(coins)
        while lim < target:
            if c < n and coins[c] <= lim + 1:
                lim += coins[c]
                c += 1
            else:
                ret += 1
                lim += lim + 1
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
