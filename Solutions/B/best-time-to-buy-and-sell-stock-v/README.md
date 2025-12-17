# Best time to buy and sell stock v

[Problem link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        full, part1, part2 = [0] * (k + 1), [-inf] * k, [-inf] * k
        for x in prices:
            for i in range(k - 1, -1, -1):
                full[i + 1] = max(full[i + 1], part1[i] + x, part2[i] - x)
                part1[i] = max(part1[i], full[i] - x)
                part2[i] = max(part2[i], full[i] + x)
        return max(full)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array)
